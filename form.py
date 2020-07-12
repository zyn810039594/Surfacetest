# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mainpage(object):
    def setupUi(self, Mainpage):
        Mainpage.setObjectName("Mainpage")
        Mainpage.resize(1920, 1080)
        Mainpage.setMinimumSize(QtCore.QSize(1280, 720))
        Mainpage.setBaseSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(Mainpage)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.Main = QtWidgets.QWidget(self.centralwidget)
        self.Main.setGeometry(QtCore.QRect(0, 0, 1420, 860))
        self.Main.setMinimumSize(QtCore.QSize(1420, 860))
        self.Main.setBaseSize(QtCore.QSize(1420, 860))
        self.Main.setObjectName("Main")
        self.Screen = QtWidgets.QFrame(self.Main)
        self.Screen.setGeometry(QtCore.QRect(67, 67, 1286, 726))
        self.Screen.setMinimumSize(QtCore.QSize(1286, 726))
        self.Screen.setBaseSize(QtCore.QSize(1286, 726))
        self.Screen.setStyleSheet("border-radius: 5px;  border: 10px groove gray;\n"
"border-style: outset;\n"
"border-color: rgb(2, 158, 255);")
        self.Screen.setFrameShape(QtWidgets.QFrame.Box)
        self.Screen.setLineWidth(3)
        self.Screen.setObjectName("Screen")
        self.ModeButtonArea = QtWidgets.QWidget(self.centralwidget)
        self.ModeButtonArea.setGeometry(QtCore.QRect(0, 860, 1420, 120))
        self.ModeButtonArea.setMinimumSize(QtCore.QSize(1420, 120))
        self.ModeButtonArea.setBaseSize(QtCore.QSize(1420, 120))
        self.ModeButtonArea.setObjectName("ModeButtonArea")
        self.Exitbutton = QtWidgets.QPushButton(self.ModeButtonArea)
        self.Exitbutton.setGeometry(QtCore.QRect(1240, 25, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Exitbutton.setFont(font)
        self.Exitbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.Exitbutton.setObjectName("Exitbutton")
        self.DebugMessageBox = QtWidgets.QWidget(self.centralwidget)
        self.DebugMessageBox.setGeometry(QtCore.QRect(0, 980, 1420, 100))
        self.DebugMessageBox.setMinimumSize(QtCore.QSize(1420, 100))
        self.DebugMessageBox.setBaseSize(QtCore.QSize(1420, 100))
        self.DebugMessageBox.setObjectName("DebugMessageBox")
        self.OpenDebugWin = QtWidgets.QPushButton(self.DebugMessageBox)
        self.OpenDebugWin.setGeometry(QtCore.QRect(1240, 10, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OpenDebugWin.setFont(font)
        self.OpenDebugWin.setStyleSheet("background-color: rgb(2, 209, 255);")
        self.OpenDebugWin.setObjectName("OpenDebugWin")
        self.SmallDebugWin = QtWidgets.QTextBrowser(self.DebugMessageBox)
        self.SmallDebugWin.setGeometry(QtCore.QRect(120, 10, 1000, 60))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        font.setKerning(False)
        self.SmallDebugWin.setFont(font)
        self.SmallDebugWin.setStyleSheet("background-color: rgb(2, 158, 255);\n"
"color: rgb(255, 255, 255);")
        self.SmallDebugWin.setFrameShape(QtWidgets.QFrame.Panel)
        self.SmallDebugWin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SmallDebugWin.setLineWidth(10)
        self.SmallDebugWin.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SmallDebugWin.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SmallDebugWin.setObjectName("SmallDebugWin")
        self.OtherArea = QtWidgets.QWidget(self.centralwidget)
        self.OtherArea.setGeometry(QtCore.QRect(1420, 640, 500, 440))
        self.OtherArea.setMinimumSize(QtCore.QSize(500, 440))
        self.OtherArea.setBaseSize(QtCore.QSize(500, 440))
        self.OtherArea.setObjectName("OtherArea")
        self.Title = QtWidgets.QWidget(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(1420, 0, 500, 40))
        self.Title.setMinimumSize(QtCore.QSize(500, 40))
        self.Title.setBaseSize(QtCore.QSize(500, 40))
        self.Title.setObjectName("Title")
        self.TitleWords = QtWidgets.QLabel(self.Title)
        self.TitleWords.setGeometry(QtCore.QRect(0, 0, 500, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TitleWords.setFont(font)
        self.TitleWords.setStyleSheet("color: rgb(88, 121, 180);")
        self.TitleWords.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TitleWords.setObjectName("TitleWords")
        self.Tab = QtWidgets.QWidget(self.centralwidget)
        self.Tab.setGeometry(QtCore.QRect(1420, 40, 500, 600))
        self.Tab.setMinimumSize(QtCore.QSize(500, 600))
        self.Tab.setBaseSize(QtCore.QSize(500, 600))
        self.Tab.setObjectName("Tab")
        self.Power = QtWidgets.QWidget(self.Tab)
        self.Power.setGeometry(QtCore.QRect(0, 40, 221, 81))
        self.Power.setAutoFillBackground(False)
        self.Power.setStyleSheet("border-image: url(:/new/pic/resource/powernov.png);")
        self.Power.setObjectName("Power")
        self.CameraTitle = QtWidgets.QWidget(self.Tab)
        self.CameraTitle.setGeometry(QtCore.QRect(130, 150, 161, 51))
        self.CameraTitle.setStyleSheet("border-image: url(:/new/pic/resource/camera.png);")
        self.CameraTitle.setObjectName("CameraTitle")
        self.OtherWords = QtWidgets.QWidget(self.Tab)
        self.OtherWords.setGeometry(QtCore.QRect(30, 220, 141, 311))
        self.OtherWords.setStyleSheet("border-image: url(:/new/pic/resource/其他文字.png);")
        self.OtherWords.setObjectName("OtherWords")
        self.A1 = QtWidgets.QSlider(self.Tab)
        self.A1.setGeometry(QtCore.QRect(180, 245, 180, 22))
        self.A1.setMinimum(0)
        self.A1.setMaximum(180)
        self.A1.setProperty("value", 90)
        self.A1.setOrientation(QtCore.Qt.Horizontal)
        self.A1.setObjectName("A1")
        self.A2 = QtWidgets.QSlider(self.Tab)
        self.A2.setGeometry(QtCore.QRect(180, 325, 180, 22))
        self.A2.setMinimum(30)
        self.A2.setMaximum(150)
        self.A2.setProperty("value", 90)
        self.A2.setOrientation(QtCore.Qt.Horizontal)
        self.A2.setObjectName("A2")
        self.A3 = QtWidgets.QSlider(self.Tab)
        self.A3.setGeometry(QtCore.QRect(180, 405, 180, 22))
        self.A3.setMinimum(30)
        self.A3.setMaximum(150)
        self.A3.setProperty("value", 90)
        self.A3.setSliderPosition(90)
        self.A3.setOrientation(QtCore.Qt.Horizontal)
        self.A3.setObjectName("A3")
        self.Led = QtWidgets.QLabel(self.Tab)
        self.Led.setGeometry(QtCore.QRect(220, 480, 101, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.Led.setFont(font)
        self.Led.setAutoFillBackground(False)
        self.Led.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.Led.setFrameShape(QtWidgets.QFrame.Panel)
        self.Led.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Led.setLineWidth(4)
        self.Led.setMidLineWidth(2)
        self.Led.setTextFormat(QtCore.Qt.AutoText)
        self.Led.setAlignment(QtCore.Qt.AlignCenter)
        self.Led.setObjectName("Led")
        self.Auto = QtWidgets.QWidget(self.Tab)
        self.Auto.setGeometry(QtCore.QRect(330, 20, 76, 111))
        self.Auto.setObjectName("Auto")
        self.AutoButton = QtWidgets.QPushButton(self.Auto)
        self.AutoButton.setGeometry(QtCore.QRect(0, 0, 76, 76))
        self.AutoButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.AutoButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"selection-color: rgb(0, 85, 0);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 35px;  border: 10px groove gray;\n"
"border-style: outset;\n"
"border-color: rgb(170, 255, 0);\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.AutoButton.setText("")
        self.AutoButton.setCheckable(True)
        self.AutoButton.setAutoDefault(False)
        self.AutoButton.setFlat(False)
        self.AutoButton.setObjectName("AutoButton")
        self.AutoText = QtWidgets.QLabel(self.Auto)
        self.AutoText.setGeometry(QtCore.QRect(0, 90, 76, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AutoText.setFont(font)
        self.AutoText.setStyleSheet("color: rgb(89, 122, 180);")
        self.AutoText.setAlignment(QtCore.Qt.AlignCenter)
        self.AutoText.setObjectName("AutoText")
        self.Auto.raise_()
        self.Power.raise_()
        self.CameraTitle.raise_()
        self.OtherWords.raise_()
        self.A1.raise_()
        self.A2.raise_()
        self.A3.raise_()
        self.Led.raise_()
        Mainpage.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mainpage)
        QtCore.QMetaObject.connectSlotsByName(Mainpage)

    def retranslateUi(self, Mainpage):
        _translate = QtCore.QCoreApplication.translate
        Mainpage.setWindowTitle(_translate("Mainpage", "Mainpage"))
        self.Exitbutton.setText(_translate("Mainpage", "EXIT"))
        self.OpenDebugWin.setText(_translate("Mainpage", "Debug\n"
"Window"))
        self.TitleWords.setText(_translate("Mainpage", "Micro White Controller Pad"))
        self.Led.setText(_translate("Mainpage", "SAFE"))
        self.AutoText.setText(_translate("Mainpage", "AUTO"))
import resource_rc
