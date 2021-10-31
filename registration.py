from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from menu import Menu


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class Registration(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        uic.loadUi('./Designs/registration.ui', self)
        self.setWindowTitle('Регистрация')
        self.run()

    def run(self):
        self.btn_ok.clicked.connect(self.check_password_and_login)

    def check_normal_password(self):
        # if len(self.ledit_password.text()) < 8:
        #     raise LengthError('Слишком короткий пароль')
        # for i in list(self.ledit_password.text()):
        #     if i.isupper():
        #         raise LetterError('Все буквы используются в верхнем регистре')
        #     if i.islower():
        #         raise LetterError('Все буквы используются в нижнем регистре')
        #     if i.isdigit():
        #         raise DigitError('В пароле нет ни одной цифры')
        return "ok"

    def check_password_and_login(self):
        self.statusBar().setStyleSheet("background-color: #FF0000")
        self.password_ok = False
        if self.ledit_login.text() == '' and self.ledit_password.text() != '':
            self.statusBar().showMessage('Введите логин')
        elif self.ledit_password.text() == '' and self.ledit_login.text() != '':
            self.statusBar().showMessage('Введите пароль')
        elif self.ledit_login.text() == '' and self.ledit_password.text() == '':
            self.statusBar().showMessage('Введите логин и пароль')
        if self.ledit_login.text() != '' and self.ledit_password.text() != '':
            self.try_except()

    def try_except(self):
        try:
            res = self.check_normal_password()
            if res == "ok":
                self.password_ok = True
                self.create_user()
                self.statusBar().showMessage('')
        except PasswordError as a:
            self.statusBar().showMessage(f"{a}")

    def create_user(self):
        res = self.db.check_login_exist(self.ledit_login.text())
        if res:
            self.statusBar().showMessage('Пользователь с таким логином уже существует')
        elif not res and self.password_ok:
            self.db.fill_user_table(self.ledit_login.text(), self.ledit_password.text())
            self.menu()

    def menu(self):
        self.st = Menu(self.db)
        self.hide()
        self.st.show()
