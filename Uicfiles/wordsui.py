# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/young_cucumber/Desktop/help/Designs/words.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 600)
        MainWindow.setStyleSheet("background-color: rgba(255, 212, 121, 128);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrlarea_words = QtWidgets.QScrollArea(self.centralwidget)
        self.scrlarea_words.setGeometry(QtCore.QRect(0, 60, 800, 501))
        self.scrlarea_words.setWidgetResizable(True)
        self.scrlarea_words.setObjectName("scrlarea_words")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 796, 497))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrlarea_words.setWidget(self.scrollAreaWidgetContents)
        self.btn_menu = QtWidgets.QPushButton(self.centralwidget)
        self.btn_menu.setGeometry(QtCore.QRect(10, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_menu.setFont(font)
        self.btn_menu.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 147, 0, 128);")
        self.btn_menu.setObjectName("btn_menu")
        self.lbl_logo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo.setGeometry(QtCore.QRect(100, 0, 281, 61))
        self.lbl_logo.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("/Users/young_cucumber/Desktop/help/Designs/../Not programming code/resized.logo.png"))
        self.lbl_logo.setObjectName("lbl_logo")
        self.btn_instruction = QtWidgets.QPushButton(self.centralwidget)
        self.btn_instruction.setGeometry(QtCore.QRect(600, 0, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_instruction.setFont(font)
        self.btn_instruction.setStyleSheet("background-color: rgba(0, 144, 81, 128);\n"
"color: rgb(255, 255, 255);")
        self.btn_instruction.setObjectName("btn_instruction")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
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
        self.btn_menu.setText(_translate("MainWindow", "Назад"))
        self.btn_instruction.setText(_translate("MainWindow", "Инструкция"))
