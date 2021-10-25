import csv
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


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
    def __init__(self):
        super().__init__()
        uic.loadUi('registration.ui', self)
        QApplication.setStyle("Fusion")
        self.setWindowTitle('Регистрация')
        self.run()

    def run(self):
        self.btn_ok.clicked.connect(self.check_password_and_login)

    def check_password_and_login(self):
        def check(self):
            mac_keyboard = list("qwertyuiop_asdfghjkl_zxcvbnm_йцукенгшщзхъ_фывапролджэё_ячсмитьбю")
            is_upper = False
            is_lower = False
            is_length = False
            is_digit = False
            is_not_combination = True
            if len(self.lbl_password) > 8:
                is_length = True
            for i in list(self.lbl_password):
                if i.isupper():
                    is_upper = True
                if i.islower():
                    is_lower = True
                if i.isdigit():
                    is_digit = True
            password = self.lbl_password.lower()
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

        try:
            res = self.check(self.lbl_password.text())
            if res == "ok":
                self.lbl_exception.setText('')
        except LengthError as a:
            self.lbl_exception.setText(f"{a}")
        except LetterError as a:
            self.lbl_exception.setText(f"{a}")
        except DigitError as a:
            self.lbl_exception.setText(f"{a}")
        except SequenceError as a:
            self.lbl_exception.setText(f"{a}")

app = QApplication(sys.argv)
ex = Registration()
ex.show()
sys.exit(app.exec())
