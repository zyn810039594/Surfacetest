# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DebugUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DebugUI(object):
    def setupUi(self, DebugUI):
        DebugUI.setObjectName("DebugUI")
        DebugUI.setWindowModality(QtCore.Qt.NonModal)
        DebugUI.setEnabled(True)
        DebugUI.resize(640, 480)
        DebugUI.setMinimumSize(QtCore.QSize(640, 480))
        DebugUI.setMaximumSize(QtCore.QSize(640, 480))
        DebugUI.setBaseSize(QtCore.QSize(640, 480))
        DebugUI.setWindowOpacity(0.6)
        DebugUI.setStyleSheet("background-color: rgb(0, 187, 255);")
        DebugUI.setSizeGripEnabled(False)
        DebugUI.setModal(False)
        self.CodeScreen = QtWidgets.QTextBrowser(DebugUI)
        self.CodeScreen.setGeometry(QtCore.QRect(0, 0, 640, 430))
        self.CodeScreen.setMinimumSize(QtCore.QSize(640, 430))
        self.CodeScreen.setMaximumSize(QtCore.QSize(640, 430))
        self.CodeScreen.setBaseSize(QtCore.QSize(640, 430))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.CodeScreen.setFont(font)
        self.CodeScreen.setStyleSheet("background-color: rgb(0, 187, 255);")
        self.CodeScreen.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CodeScreen.setLineWidth(0)
        self.CodeScreen.setObjectName("CodeScreen")
        self.CodeTypein = QtWidgets.QTextEdit(DebugUI)
        self.CodeTypein.setGeometry(QtCore.QRect(0, 430, 560, 50))
        self.CodeTypein.setMinimumSize(QtCore.QSize(560, 50))
        self.CodeTypein.setMaximumSize(QtCore.QSize(560, 50))
        self.CodeTypein.setSizeIncrement(QtCore.QSize(0, 0))
        self.CodeTypein.setBaseSize(QtCore.QSize(560, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        self.CodeTypein.setFont(font)
        self.CodeTypein.setTabletTracking(False)
        self.CodeTypein.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CodeTypein.setStyleSheet("background-color: rgb(30, 200, 255);")
        self.CodeTypein.setFrameShape(QtWidgets.QFrame.Box)
        self.CodeTypein.setLineWidth(1)
        self.CodeTypein.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CodeTypein.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CodeTypein.setObjectName("CodeTypein")
        self.Send = QtWidgets.QPushButton(DebugUI)
        self.Send.setGeometry(QtCore.QRect(560, 430, 80, 25))
        self.Send.setObjectName("Send")
        self.Back = QtWidgets.QPushButton(DebugUI)
        self.Back.setGeometry(QtCore.QRect(560, 455, 80, 25))
        self.Back.setObjectName("Back")

        self.retranslateUi(DebugUI)
        QtCore.QMetaObject.connectSlotsByName(DebugUI)

    def retranslateUi(self, DebugUI):
        _translate = QtCore.QCoreApplication.translate
        DebugUI.setWindowTitle(_translate("DebugUI", "DebugUI"))
        self.CodeTypein.setPlaceholderText(_translate("DebugUI", "Please type code here."))
        self.Send.setText(_translate("DebugUI", "Send"))
        self.Back.setText(_translate("DebugUI", "Back"))
