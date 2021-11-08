from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from constants import *
from cards import Cards
from favourites import Favourites
from test import Test
from words import Words


class Menu(QMainWindow):
    def __init__(self, db):
        super().__init__()
        uic.loadUi(FILE_MENU, self)
        self.db = db
        self.setWindowTitle(MENU_TITLE)
        self.run()

    def run(self):
        self.btn_cards.clicked.connect(self.cards)
        self.btn_favourites.clicked.connect(self.favourites)
        self.btn_words.clicked.connect(self.words)
        self.btn_test.clicked.connect(self.test)

    # Открытие окна "Карточки"
    def cards(self):
        self.st = Cards(self.db, self)
        self.hide()
        self.st.show()

    # Открытие окна "Тест"
    def test(self):
        self.st = Test(self.db, self)
        self.hide()
        self.st.show()

    # Открытие окна "Все слова"
    def words(self):
        self.st = Words(self.db, self)
        self.hide()
        self.st.show()

    # Открытие окна "Избранное"
    def favourites(self):
        self.st = Favourites(self.db, self)
        self.hide()
        self.st.show()
