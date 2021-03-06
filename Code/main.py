import sys

from start import Entre
from adjust_db import DataBase
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    db = DataBase()
    ex = Entre(db)
    ex.show()
    sys.exit(app.exec())