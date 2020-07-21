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

up=bool(False)
down=bool(False)
left=bool(False)
right=bool(False)

RunFlag=True

net=NetHandle.NetTransmit()

class MyWindow(QMainWindow, Ui_Mainpage):
    url = "http://192.168.1.3:6000/?action=stream?dummy=param.mjpg"
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # self.VideoInit()
        self.ButtonInit()

    def VideoInit(self):
        self.cap = cv2.VideoCapture(self.url)
        self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        VideoTh=threading.Thread(target=self.VideoDisplay)
        VideoTh.setDaemon(True)
        VideoTh.start()

    def ButtonInit(self):
        self.Exitbutton.clicked.connect(self.CloseApp)
        self.OpenDebugWin.clicked.connect(self.DisPlayDebugWindow)

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_W):
            self.SmallDebugWin.setText('测试：up')
            up=True
        if (event.key() == Qt.Key_S):
            self.SmallDebugWin.setText('测试：down')
            down=True
        if (event.key() == Qt.Key_A):
            self.SmallDebugWin.setText('测试：left')
            left=True
        if (event.key() == Qt.Key_D):
            self.SmallDebugWin.setText('测试：right')
            right=True

    def VideoDisplay(self):
        while self.cap.isOpened() and RunFlag:
            success,frame=self.cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.ScreenPic.setPixmap(QtGui.QPixmap.fromImage(img))
            self.ui.DisplayLabel.setScaledContents(True)
    def DisPlayDebugWindow(self):
        DebugWin=DebugWindow()
        DebugWin.exec_()

    def RunSend(self):
        while RunFlag:
            DataBytes=net.Receive()
            DataString=binascii.hexlify(DataBytes)
            DataString=DataString.decode()
            self.SmallDebugWin.setText(DataString)
            DataBytes
            SendByteStr = b"\xff\xee\x00\x00\x00\x00\x00\x00\x00\x00\x00\xef\xfe"


    def CloseApp(self):
        RunFlag=False
        QCoreApplication.quit()
        net.DeInit()

class DebugWindow(QDialog,Ui_DebugUI):
    SendFlag=False
    def __init__(self,parent=None):
        super(DebugWindow,self).__init__(parent)
        self.setupUi(self)
        self.ButtonInit()
        self.setWindowFlags(Qt.FramelessWindowHint)
        DisTh=threading.Thread(target=self.DebugRun)
        DisTh.setDaemon(True)
        DisTh.start()

    def ButtonInit(self):
        self.Send.clicked.connect(self.SendButton)
        self.Back.clicked.connect(self.WinClose)

    def SendButton(self):
        TextToSend = self.CodeTypein.toPlainText()
        self.CodeScreen.append(TextToSend)
        BytesToSend = bytes(binascii.unhexlify(TextToSend))
        net.Send(Data=BytesToSend)

    def DebugRun(self):
        while RunFlag:
            DataBytes=net.Receive()
            DataString=binascii.hexlify(DataBytes)
            DataString=DataString.decode()
            self.CodeScreen.append(DataString)
            self.CodeScreen.moveCursor(self.CodeScreen.textCursor().End)
    def WinClose(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    net.Init()
    MainWindow = MyWindow()
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
