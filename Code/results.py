import csv
import os

from test import *
from constants import *
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5 import QtWidgets
from uicfiles.resultui import Ui_MainWindow

vowels = 'ауоыиэяюёе'


class Results(QMainWindow, Ui_MainWindow):
    def __init__(self, answers, keys, test):
        super().__init__()
        self.setupUi(self)
        self.answers = answers
        self.keys = keys
        self.test = test
        self.run()
        self.set_image()

    def set_image(self):
        self.pixmap = QPixmap(IMAGE_RESIZED)
        self.lbl_logo.setPixmap(self.pixmap)

    def run(self):
        self.loadtable()
        self.btn_menu.clicked.connect(self.test_return)

    # Создание таблицы и занесение в нее данных с выбранными ответами и правильными
    def loadtable(self):
        with open('res.csv', encoding='utf-8', mode='w') as csvfile:
            self.tablewdgt.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tablewdgt.setColumnCount(3)
            self.tablewdgt.setRowCount(len(self.answers))
            for i, word in enumerate(self.answers):
                self.tablewdgt.setItem(i, 0, QTableWidgetItem(word))
            for j, key in enumerate(self.keys):
                self.tablewdgt.setItem(j, 1, QTableWidgetItem(key))
            self.set_score()
            self.compute_result()
        self.tablewdgt.resizeColumnsToContents()

    # Расставление баллов
    def set_score(self):
        for i in range(len(self.answers)):
            if str(self.tablewdgt.item(i, 0).text()) == str(self.tablewdgt.item(i, 1).text()):
                self.tablewdgt.setItem(i, 2, QTableWidgetItem('1'))
            else:
                self.tablewdgt.setItem(i, 2, QTableWidgetItem('0'))
        header = self.tablewdgt.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    # Подсчет результатов
    def compute_result(self):
        summ = 0
        for i in range(len(self.answers)):
            summ += int(self.tablewdgt.item(i, 2).text())
        self.ledit_total.setText(str(summ))
        self.ledit_total.setEnabled(False)

    # Вернуться к тесту
    def test_return(self):
        os.remove("res.csv")
        self.st = self.test
        self.hide()
        self.st.show()

