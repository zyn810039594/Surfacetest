import sys
import threading
import NetHandle
import cv2
import time
import binascii

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from form import *
from DebugUI import *
from DataAnalyse import *

up = False
down = False
left = False
right = False

A1Bar_L = False
A1Bar_R = False
A2Bar_L = False
A2Bar_R = False
A3Bar_L = False
A3Bar_R = False

straight = 128
side = 128

RecFlag = False
SendFlag = True
RunFlag = True

state = 0
power = 0
danger = 0

acc = {0.0, 0.0, 0.0}
pal = {0.0, 0.0, 0.0}
eul = {0.0, 0.0, 0.0}

DataBytes = bytes(0)

net = NetHandle.NetTransmit()


class MyWindow(QMainWindow, Ui_Mainpage):
    url = "http://192.168.2.1:7000/?action=stream?dummy=param.mjpg"
    DebugWinFlag = False
    DateBytes = bytes(0)

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.VideoInit()
        self.ButtonInit()
        self.StartTransmit()
        self.DisplayInit()

    def VideoInit(self):
        VideoTh = threading.Thread(target=self.VideoDisplay)
        VideoTh.setDaemon(True)
        VideoTh.start()

    def ButtonInit(self):
        self.Exitbutton.clicked.connect(self.CloseApp)
        self.OpenDebugWin.clicked.connect(self.DisPlayDebugWindow)
        KeyTh = threading.Thread(target=self.KeyFlash)
        KeyTh.setDaemon(True)
        KeyTh.start()

    def DisplayInit(self):
        DisTh = threading.Thread(target=self.DisPlayReflash)
        DisTh.setDaemon(True)
        DisTh.start()

    def keyPressEvent(self, event):
        global straight, side, up, down, left, right, A1Bar_L, A1Bar_R, A2Bar_L, A2Bar_R, A3Bar_L, A3Bar_R
        if event.key() == Qt.Key_W:
            up = True
        if event.key() == Qt.Key_S:
            down = True
        if event.key() == Qt.Key_A:
            left = True
        if event.key() == Qt.Key_D:
            right = True
        if event.key() == Qt.Key_Y:
            A1Bar_L = True
        if event.key() == Qt.Key_U:
            A1Bar_R = True
        if event.key() == Qt.Key_H:
            A2Bar_L = True
        if event.key() == Qt.Key_J:
            A2Bar_R = True
        if event.key() == Qt.Key_N:
            A3Bar_L = True
        if event.key() == Qt.Key_M:
            A3Bar_R = True

    def keyReleaseEvent(self, event):
        global up, down, left, right, A1Bar_L, A1Bar_R, A2Bar_L, A2Bar_R, A3Bar_L, A3Bar_R
        if event.key() == Qt.Key_W:
            up = False
        if event.key() == Qt.Key_S:
            down = False
        if event.key() == Qt.Key_A:
            left = False
        if event.key() == Qt.Key_D:
            right = False
        if event.key() == Qt.Key_Y:
            A1Bar_L = False
        if event.key() == Qt.Key_U:
            A1Bar_R = False
        if event.key() == Qt.Key_H:
            A2Bar_L = False
        if event.key() == Qt.Key_J:
            A2Bar_R = False
        if event.key() == Qt.Key_N:
            A3Bar_L = False
        if event.key() == Qt.Key_M:
            A3Bar_R = False

    def VideoDisplay(self):
        self.cap = cv2.VideoCapture(self.url)
        self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        while self.cap.isOpened() and RunFlag:
            self.cap = cv2.VideoCapture(self.url)
            self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
            success, frame = self.cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.ScreenPic.setPixmap(QtGui.QPixmap.fromImage(img))

    def DisPlayDebugWindow(self):
        self.DebugWinFlag = True
        DebugWin = DebugWindow()
        DebugWin.exec_()

    def StartTransmit(self):
        TransmitTh = threading.Thread(target=self.RunIO)
        TransmitTh.setDaemon(True)
        TransmitTh.start()

    def RunIO(self):
        global state, power, danger, acc, pal, eul, SendFlag, RecFlag
        while RunFlag:
            DataBytes = net.Receive()

            state, power, danger, acc, pal, eul = Analyse().BaseIn(datahex=DataBytes)
            if not RecFlag:
                RecFlag = True
            BackText, Send_Bytes, self.Send_Str = Analyse().BaseOut(straight=straight, side=side,
                                                                    A1V=self.A1.value(), A2V=self.A2.value(),
                                                                    A3V=self.A3.value())
            if not self.DebugWinFlag:
                net.Send(Data=Send_Bytes)
            if not SendFlag:
                SendFlag = True

    def DisPlayReflash(self):
        global RecFlag, SendFlag
        while RunFlag:
            DataString = binascii.hexlify(DataBytes)
            DataString = DataString.decode()
            # self.SmallDebugWin.setText('straight:' + str(straight) + ' side:' + str(side))
            if RecFlag:
                RecFlag = False
                self.SmallDebugWin.setText(DataString)
                if self.DebugWinFlag:
                    DebugWindow.CodeScreen.append('RX:' + DataString)
            if state != 0:
                if danger == 0:
                    self.Led.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.Led.setText("SAFE")
                elif danger == 1:
                    self.Led.setStyleSheet("background-color: rgb(255, 255, 0);")
                    self.Led.setText("CARE")
                elif danger == 2:
                    self.Led.setStyleSheet("background:rgb(255,0,0);")
                    self.Led.setText("WARN")
            if self.DebugWinFlag:
                if SendFlag:
                    SendFlag = False
                    DebugWindow.CodeScreen.append('TX:' + self.Send_Str)
                self.CodeScreen.moveCursor(self.CodeScreen.textCursor().End)

    def KeyFlash(self):
        global straight, side
        while RunFlag:
            if up:
                if straight < 250:
                    straight += 5
                else:
                    straight = 255
            if down:
                if straight > 5:
                    straight -= 5
                else:
                    straight = 0
            if left:
                if side < 250:
                    side += 5
                else:
                    side = 255
            if right:
                if side > 5:
                    side -= 5
                else:
                    side = 0
            if A1Bar_L:
                temp = self.A1.value()
                if temp > 0:
                    self.A1.setValue(temp - 1)
            if A1Bar_R:
                temp = self.A1.value()
                if temp < 255:
                    self.A1.setValue(temp + 1)
            if A2Bar_L:
                temp = self.A2.value()
                if temp > 0:
                    self.A2.setValue(temp - 1)
            if A2Bar_R:
                temp = self.A2.value()
                if temp < 255:
                    self.A2.setValue(temp + 1)
            if A3Bar_L:
                temp = self.A3.value()
                if temp > 0:
                    self.A3.setValue(temp - 1)
            if A3Bar_R:
                temp = self.A3.value()
                if temp < 255:
                    self.A3.setValue(temp + 1)
            if straight > 128:
                straight -= 1
            elif straight < 128:
                straight += 1
            if side > 128:
                side -= 1
            elif side < 128:
                side += 1
            time.sleep(0.005)

    def CloseApp(self):
        global RunFlag
        RunFlag = False
        self.SmallDebugWin.setText("程序关闭")
        QCoreApplication.quit()
        net.DeInit()


class DebugWindow(QDialog, Ui_DebugUI):
    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setupUi(self)
        self.ButtonInit()
        self.setWindowFlags(Qt.FramelessWindowHint)

    def ButtonInit(self):
        self.Send.clicked.connect(self.SendButton)
        self.Back.clicked.connect(self.WinClose)

    def SendButton(self):
        TextToSend = self.CodeTypein.toPlainText()
        self.CodeScreen.append(TextToSend)
        BytesToSend = bytes.fromhex(TextToSend)
        net.Send(Data=BytesToSend)

    def WinClose(self):
        MainWindow.DebugWinFlag = False
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    net.Init()
    MainWindow = MyWindow()
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
