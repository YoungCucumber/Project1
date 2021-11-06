from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from menu import Menu
from constants import *


class Registration(QMainWindow):
    def __init__(self, db, start):
        super().__init__()
        self.db = db
        self.start = start
        uic.loadUi(FILE_REGISTRATION, self)
        self.setWindowTitle(REGISTRATION_TITLE)
        self.run()

    def run(self):
        self.btn_ok.clicked.connect(self.check_password_and_login)

    # Проверка на корректность вводимых данных
    def check_password_and_login(self):
        self.statusBar().setStyleSheet(EXCEPTION_STATUSBAR)
        if self.ledit_login.text() == EMPTY_LINE or self.ledit_password.text() == EMPTY_LINE:
            self.start.check_empty_lines(self)
        else:
            self.create_user()

    # Создание нового пользователя и занесение его в таблицу базы данных Users
    def create_user(self):
        # Проверка на то, что такого логина еще не существует
        res = self.db.check_login_exist(self.ledit_login.text())
        if res:
            self.statusBar().showMessage(LOGIN_EXIST)
        elif not res:
            self.db.fill_user_table(self.ledit_login.text(), self.ledit_password.text())
            self.menu()

    # Открытие окна "Меню"
    def menu(self):
        self.st = Menu(self.db)
        self.hide()
        self.st.show()
