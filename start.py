from registration import Registration
from menu import Menu
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Entre(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        uic.loadUi('./Designs/start.ui', self)
        QApplication.setStyle('Windows')
        self.setWindowTitle('Вход')
        self.run()

    def run(self):
        self.btn_entre.clicked.connect(self.check)
        self.btn_registration.clicked.connect(self.registration)

    def registration(self):
        self.st = Registration(self.db)
        self.hide()
        self.st.show()

    def check(self):
        self.statusBar().setStyleSheet("background-color: #FF0000")
        # проверка на пустые поля
        if self.ledit_login.text() == '' and self.ledit_password.text() != '':
            self.statusBar().showMessage('Введите логин')
        elif self.ledit_password.text() == '' and self.ledit_login.text() != '':
            self.statusBar().showMessage('Введите пароль')
        elif self.ledit_login.text() == '' and self.ledit_password.text() == '':
            self.statusBar().showMessage('Введите логин и пароль')
        else:
            if self.db.check_login_exist(self.ledit_login.text()):
                if self.db.check_right_password(self.ledit_password.text(), self.ledit_login.text()):
                    self.menu()
                else:
                    self.statusBar().showMessage('Неверный пароль')
            else:
                self.statusBar().showMessage('Нет пользователя с таким логином')

    def menu(self):
        self.st = Menu(self.db)
        self.hide()
        self.st.show()