# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/young_cucumber/Desktop/help/cards.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgba(255, 212, 121, 128);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_menu = QtWidgets.QPushButton(self.centralwidget)
        self.btn_menu.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.btn_menu.setStyleSheet("background-color: rgba(255, 147, 0, 128);\n"
"color: rgb(255, 255, 255);")
        self.btn_menu.setObjectName("btn_menu")
        self.btn_card = QtWidgets.QPushButton(self.centralwidget)
        self.btn_card.setGeometry(QtCore.QRect(210, 120, 361, 321))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_card.setFont(font)
        self.btn_card.setStyleSheet("background-color: rgba(169, 169, 169, 128);\n"
"color: rgb(255, 255, 255);")
        self.btn_card.setObjectName("btn_card")
        self.lbl_logo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo.setGeometry(QtCore.QRect(120, 10, 321, 91))
        self.lbl_logo.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("/Users/young_cucumber/Desktop/help/../Not programming code/logo.png"))
        self.lbl_logo.setObjectName("lbl_logo")
        self.checkbox_addfavourites = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_addfavourites.setGeometry(QtCore.QRect(20, 450, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.checkbox_addfavourites.setFont(font)
        self.checkbox_addfavourites.setStyleSheet("background-color: rgba(255, 147, 0, 0);")
        self.checkbox_addfavourites.setObjectName("checkbox_addfavourites")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(610, 150, 131, 261))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_next.setFont(font)
        self.btn_next.setStyleSheet("background-color: rgba(255, 147, 0, 128);\n"
"color: rgb(255, 255, 255);")
        self.btn_next.setObjectName("btn_next")
        self.btn_complete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_complete.setGeometry(QtCore.QRect(40, 150, 131, 261))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_complete.setFont(font)
        self.btn_complete.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 144, 81, 128);")
        self.btn_complete.setObjectName("btn_complete")
        self.progressbr = QtWidgets.QProgressBar(self.centralwidget)
        self.progressbr.setGeometry(QtCore.QRect(10, 510, 781, 23))
        self.progressbr.setStyleSheet("background-color: rgba(255, 212, 121, 0);")
        self.progressbr.setProperty("value", 24)
        self.progressbr.setObjectName("progressbr")
        self.lbl_show = QtWidgets.QLabel(self.centralwidget)
        self.lbl_show.setGeometry(QtCore.QRect(210, 60, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_show.setFont(font)
        self.lbl_show.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lbl_show.setObjectName("lbl_show")
        self.spnbox_amount = QtWidgets.QSpinBox(self.centralwidget)
        self.spnbox_amount.setGeometry(QtCore.QRect(610, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spnbox_amount.setFont(font)
        self.spnbox_amount.setStyleSheet("background-color: rgba(255, 38, 0, 41);\n"
"color: rgb(255, 255, 255);")
        self.spnbox_amount.setMaximum(476)
        self.spnbox_amount.setObjectName("spnbox_amount")
        self.lbl_choose = QtWidgets.QLabel(self.centralwidget)
        self.lbl_choose.setGeometry(QtCore.QRect(560, 10, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_choose.setFont(font)
        self.lbl_choose.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.lbl_choose.setObjectName("lbl_choose")
        self.btn_apply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_apply.setGeometry(QtCore.QRect(700, 80, 81, 26))
        self.btn_apply.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(4, 51, 255, 82);")
        self.btn_apply.setObjectName("btn_apply")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_menu.setText(_translate("MainWindow", "??????????"))
        self.btn_card.setText(_translate("MainWindow", "?????? ???????????? ????????????????\n"
" ???????????????? ????????????????????\n"
" ????????????????"))
        self.checkbox_addfavourites.setText(_translate("MainWindow", "???????????????? ?????????? ?? \"??????????????????\""))
        self.btn_next.setText(_translate("MainWindow", "??????????????????"))
        self.btn_complete.setText(_translate("MainWindow", "??????????????"))
        self.lbl_show.setText(_translate("MainWindow", "??????????????, ?????????? ???????????????????? ??????????"))
        self.lbl_choose.setText(_translate("MainWindow", "???????????????? ???????????????????? ????????????????"))
        self.btn_apply.setText(_translate("MainWindow", "??????????????????"))
