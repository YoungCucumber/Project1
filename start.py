from registration import Registration
from constants import *
from menu import Menu
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Entre(QMainWindow):
    def __init__(self, db, app):
        super().__init__()
        self.db = db
        uic.loadUi(FILE_ENTRE, self)
        app.setStyle('Windows')
        self.setWindowTitle(ENTRE_TITLE)
        self.run()

    def run(self):
        self.btn_entre.clicked.connect(self.check)
        self.btn_registration.clicked.connect(self.registration)

    def registration(self):
        self.st = Registration(self.db, self)
        self.hide()
        self.st.show()

    def check(self):
        self.statusBar().setStyleSheet(EXCEPTION_STATUSBAR)
        # проверка на пустые поля
        if self.ledit_login.text() == EMPTY_LINE or self.ledit_password.text() == EMPTY_LINE:
            self.check_empty_lines()
        else:
            if self.db.check_login_exist(self.ledit_login.text()):
                if self.db.check_right_password(self.ledit_password.text(), self.ledit_login.text()):
                    self.menu()
                else:
                    self.statusBar().showMessage(EXCEPTION_PASSWORD)
            else:
                self.statusBar().showMessage(EXCEPTION_LOGIN)

    def check_empty_lines(self):
        if self.ledit_login.text() == EMPTY_LINE and self.ledit_password.text() != EMPTY_LINE:
            self.statusBar().showMessage(ENTER_LOGIN)
        elif self.ledit_password.text() == EMPTY_LINE and self.ledit_login.text() != EMPTY_LINE:
            self.statusBar().showMessage(ENTER_PASSWORD)
        elif self.ledit_login.text() == EMPTY_LINE and self.ledit_password.text() == EMPTY_LINE:
            self.statusBar().showMessage(ENTER_LOGIN_PASSWORD)

    def menu(self):
        self.st = Menu(self.db)
        self.hide()
        self.st.show()