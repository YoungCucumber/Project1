# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/young_cucumber/Desktop/help/registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_start_window(object):
    def setupUi(self, start_window):
        start_window.setObjectName("start_window")
        start_window.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(start_window.sizePolicy().hasHeightForWidth())
        start_window.setSizePolicy(sizePolicy)
        start_window.setStyleSheet("background-color: rgba(255, 212, 121, 128);")
        self.centralwidget = QtWidgets.QWidget(start_window)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_entre = QtWidgets.QLabel(self.centralwidget)
        self.lbl_entre.setGeometry(QtCore.QRect(190, 140, 431, 61))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_entre.setFont(font)
        self.lbl_entre.setStyleSheet("background-color: rgba(255, 212, 121, 0);\n"
"color: rgb(255, 255, 255);")
        self.lbl_entre.setObjectName("lbl_entre")
        self.ledit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.ledit_login.setGeometry(QtCore.QRect(230, 250, 321, 31))
        self.ledit_login.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.ledit_login.setObjectName("ledit_login")
        self.ledit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.ledit_password.setGeometry(QtCore.QRect(230, 310, 321, 31))
        self.ledit_password.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.ledit_password.setObjectName("ledit_password")
        self.lbl_logo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo.setGeometry(QtCore.QRect(240, 30, 321, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_logo.sizePolicy().hasHeightForWidth())
        self.lbl_logo.setSizePolicy(sizePolicy)
        self.lbl_logo.setStyleSheet("background-color: rgba(255, 212, 121, 0);")
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("/Users/young_cucumber/Desktop/help/../Not programming code/logo.png"))
        self.lbl_logo.setObjectName("lbl_logo")
        self.lbl_login = QtWidgets.QLabel(self.centralwidget)
        self.lbl_login.setGeometry(QtCore.QRect(230, 220, 111, 20))
        self.lbl_login.setStyleSheet("background-color: rgba(255, 212, 121, 0);\n"
"color: rgb(255, 255, 255);")
        self.lbl_login.setObjectName("lbl_login")
        self.lbl_password = QtWidgets.QLabel(self.centralwidget)
        self.lbl_password.setGeometry(QtCore.QRect(230, 290, 60, 16))
        self.lbl_password.setStyleSheet("background-color: rgba(255, 212, 121, 0);\n"
"color: rgb(255, 255, 255);")
        self.lbl_password.setObjectName("lbl_password")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(350, 360, 81, 31))
        self.btn_ok.setStyleSheet("background-color: rgba(255, 147, 0, 128);\n"
"color: rgb(255, 255, 255);")
        self.btn_ok.setObjectName("btn_ok")
        start_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(start_window)
        self.statusbar.setObjectName("statusbar")
        start_window.setStatusBar(self.statusbar)

        self.retranslateUi(start_window)
        QtCore.QMetaObject.connectSlotsByName(start_window)

    def retranslateUi(self, start_window):
        _translate = QtCore.QCoreApplication.translate
        start_window.setWindowTitle(_translate("start_window", "?????????????????? ??????????"))
        self.lbl_entre.setText(_translate("start_window", "??????????????????????"))
        self.lbl_login.setText(_translate("start_window", "??????????"))
        self.lbl_password.setText(_translate("start_window", "????????????"))
        self.btn_ok.setText(_translate("start_window", "OK"))
