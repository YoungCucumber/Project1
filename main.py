import sys

from start import Entre
from adjust_db import DataBase
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
db = DataBase()
ex = Entre(db)
ex.show()
sys.exit(app.exec())