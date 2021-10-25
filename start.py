import csv
import sys

# from registration_window import Registration
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Entre(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui', self)
        QApplication.setStyle("Fusion")
        self.setWindowTitle('Вход')
        # self.run()

    # def run(self):
        # self.btn_registration.clicked.connect(self.registration)
        # self.btn_entre.clicked.connect(self.check)

    # def registration(self):
    #     print(12345)
    #     self.st = Registration(self)
    #     self.hide()
    #     self.st.show()
    #
    # def exit(self):
    #     sys.exit(0)

app = QApplication(sys.argv)
ex = Entre()
ex.show()
sys.exit(app.exec())
