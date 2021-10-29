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


class SequenceError(PasswordError):
    pass


class Registration(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        uic.loadUi('./Designs/registration.ui', self)
        QApplication.setStyle("Fusion")
        self.setWindowTitle('Регистрация')
        self.run()

    def run(self):
        self.btn_ok.clicked.connect(self.check_password_and_login)

    def check_normal_password(self):
        mac_keyboard = list("qwertyuiop_asdfghjkl_zxcvbnm_йцукенгшщзхъ_фывапролджэё_ячсмитьбю")
        is_upper = False
        is_lower = False
        is_length = False
        is_digit = False
        is_not_combination = True
        if len(self.ledit_password.text()) > 8:
            is_length = True
        for i in list(self.ledit_password.text()):
            if i.isupper():
                is_upper = True
            if i.islower():
                is_lower = True
            if i.isdigit():
                is_digit = True
        password = self.ledit_password.text().lower()
        for i in range(len(password) - 2):
            if password[i].isalpha() and password[i + 1].isalpha() and password[i + 2].isalpha():
                temp_letter_index = mac_keyboard.index(password[i])
                if temp_letter_index < len(mac_keyboard) - 3:
                    if password[i + 1] == mac_keyboard[temp_letter_index + 1] \
                            and password[i + 2] == mac_keyboard[temp_letter_index + 2]:
                        is_not_combination = False
                        break

        if not is_length:
            raise LengthError('Слишком короткий пароль')
        elif not (is_upper and is_lower):
            raise LetterError('Все буквы используются в нижем регистре')
        elif not is_digit:
            raise DigitError('В пароле нет ни одной цифры')
        elif not is_not_combination:
            raise SequenceError('Пароль легко подобрать')
        else:
            return "ok"

    def check_password_and_login(self):
        self.statusBar().setStyleSheet("background-color: #FF0000")
        password_ok = False
        # проверка на пустые поля
        if self.ledit_login.text() == '' and self.ledit_password.text() != '':
            self.statusBar().showMessage('Введите логин')
        elif self.ledit_password.text() == '' and self.ledit_login.text() != '':
            self.statusBar().showMessage('Введите пароль')
        elif self.ledit_login.text() == '' and self.ledit_password.text() == '':
            self.statusBar().showMessage('Введите логин и пароль')
        # проверки на надежность пароля
        if self.ledit_login.text() != '' and self.ledit_password.text() != '':
            try:
                res = self.check_normal_password()
                if res == "ok":
                    password_ok = True
                    self.statusBar().showMessage('')
            except LengthError as a:
                self.statusBar().showMessage(f"{a}")
            except LetterError as a:
                self.statusBar().showMessage(f"{a}")
            except DigitError as a:
                self.statusBar().showMessage(f"{a}")
            except SequenceError as a:
                self.statusBar().showMessage(f"{a}")
            # проверка логина
        res = self.db.check_exist_login_registration(self.ledit_login.text())
        if res:
            self.statusBar().showMessage('Пользователь с таким логином уже существует')
        elif not res and password_ok:
            self.db.fill_user_table(self.ledit_login.text(), self.ledit_password.text())
            self.menu()

    def menu(self):
        self.st = Menu(self.db)
        self.hide()
        self.st.show()