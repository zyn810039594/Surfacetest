import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from form import *

class MyWindow(QMainWindow, Ui_Mainpage):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setupUi(self)
        self.Video = QWebEngineView(self.Screen)
        self.Video.setGeometry(QtCore.QRect(3,3,1280,720))
        self.Video.setMinimumSize(QtCore.QSize(1280,720))
        self.Video.setBaseSize(QtCore.QSize(1280,720))
        self.Video.load(QtCore.QUrl('http://www.baidu.com'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
