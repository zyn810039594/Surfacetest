import sys
import asyncio
import threading
from NetHandle import NetTransmit

from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from form import *
from DebugUI import *

up=bool(False)
down=bool(False)
left=bool(False)
right=bool(False)

class MyWindow(QMainWindow, Ui_Mainpage):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setupUi(self)
        self.Video = QWebEngineView(self.Screen)
        self.Video.setGeometry(QtCore.QRect(3,3,1280,720))
        self.Video.setMinimumSize(QtCore.QSize(1280,720))
        self.Video.setBaseSize(QtCore.QSize(1280,720))
        self.Video.load(QtCore.QUrl('http://www.baidu.com'))

        self.Exitbutton.clicked.connect(QCoreApplication.quit)

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Up):
            self.SmallDebugWin.setText('测试：up')
            up=True
        if (event.key() == Qt.Key_Down):
            self.SmallDebugWin.setText('测试：down')
            down=True
        if (event.key() == Qt.Key_Left):
            self.SmallDebugWin.setText('测试：left')
            left=True
        if (event.key() == Qt.Key_Right):
            self.SmallDebugWin.setText('测试：right')
            right=True
        if (event.key() == Qt.Key_Space):
            self.SmallDebugWin.setText('测试：Space')






class DebugWindow(QDialog,Ui_DebugUI):
    def __init__(self,parent=None):
        super(DebugWindow,self).__init__(parent)
        self.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.showFullScreen()
    NetTransmit.Net_Init()
    NetTransmit.Net_Send()

    sys.exit(app.exec_())
