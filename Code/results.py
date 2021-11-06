import csv
import os

from constants import *
from test import *
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from PyQt5 import uic
from PyQt5 import QtWidgets

vowels = 'ауоыиэяюёе'


class Results(QMainWindow):
    def __init__(self, answers, keys, test):
        super().__init__()
        uic.loadUi(FILE_RESULTS, self)
        self.answers = answers
        self.keys = keys
        self.test = test
        self.setWindowTitle(RESULTS_TITLE)
        self.run()

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

