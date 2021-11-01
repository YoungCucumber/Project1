from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from menu import Menu


class Registration(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        uic.loadUi('./Designs/registration.ui', self)
        self.setWindowTitle('Регистрация')
        self.run()

    def run(self):
        self.btn_ok.clicked.connect(self.check_password_and_login)

    def check_password_and_login(self):
        self.statusBar().setStyleSheet("background-color: #FF0000")
        if self.ledit_login.text() == '' and self.ledit_password.text() != '':
            self.statusBar().showMessage('Введите логин')
        elif self.ledit_password.text() == '' and self.ledit_login.text() != '':
            self.statusBar().showMessage('Введите пароль')
        elif self.ledit_login.text() == '' and self.ledit_password.text() == '':
            self.statusBar().showMessage('Введите логин и пароль')
        if self.ledit_login.text() != '' and self.ledit_password.text() != '':
            self.create_user()

    def create_user(self):
        res = self.db.check_login_exist(self.ledit_login.text())
        if res:
            self.statusBar().showMessage('Пользователь с таким логином уже существует')
        elif not res:
            self.db.fill_user_table(self.ledit_login.text(), self.ledit_password.text())
            self.menu()

    def menu(self):
        self.st = Menu(self.db)
        self.hide()
        self.st.show()
