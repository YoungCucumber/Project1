from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from menu import Menu
from constants import *


class Registration(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        uic.loadUi(FILE_REGISTRATION, self)
        self.setWindowTitle(REGISTRATION_TITLE)
        self.run()

    def run(self):
        self.btn_ok.clicked.connect(self.check_password_and_login)

    def check_password_and_login(self):
        self.statusBar().setStyleSheet(EXCEPTION_STATUSBAR)
        if self.ledit_login.text() == EMPTY_LINE and self.ledit_password.text() != EMPTY_LINE:
            self.statusBar().showMessage(ENTER_LOGIN)
        elif self.ledit_password.text() == EMPTY_LINE and self.ledit_login.text() != EMPTY_LINE:
            self.statusBar().showMessage(ENTER_PASSWORD)
        elif self.ledit_login.text() == EMPTY_LINE and self.ledit_password.text() == EMPTY_LINE:
            self.statusBar().showMessage(ENTER_LOGIN_PASSWORD)
        if self.ledit_login.text() != EMPTY_LINE and self.ledit_password.text() != EMPTY_LINE:
            self.create_user()

    def create_user(self):
        res = self.db.check_login_exist(self.ledit_login.text())
        if res:
            self.statusBar().showMessage(LOGIN_EXIST)
        elif not res:
            self.db.fill_user_table(self.ledit_login.text(), self.ledit_password.text())
            self.menu()

    def menu(self):
        self.st = Menu(self.db)
        self.hide()
        self.st.show()
