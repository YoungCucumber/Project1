from PyQt5 import uic, QtWidgets
from cards import Cards
# from favourites import Favourites
# from test import Test
# from theory import Theory
# from words import Words
from PyQt5.QtWidgets import QApplication, QMainWindow


class Menu(QMainWindow):
    def __init__(self, db):
        super().__init__()
        uic.loadUi('./Designs/menu.ui', self)
        self.db = db
        self.setWindowTitle('Меню')
        self.run()

    def run(self):
        self.btn_cards.clicked.connect(self.cards)
        # self.btn_favourites.clicked.connect(self.favourites)
        # self.btn_words.clicked.connect(self.words)
        # self.btn_theory.clicked.connect(self.theory)
        # self.btn_test.clicked.connect(self.test)

    def cards(self):
        self.st = Cards(self.db, self)
        self.hide()
        self.st.show()

    # def theory(self):
    #     self.st = Theory()
    #     self.hide()
    #     self.st.show()
    #
    # def test(self):
    #     self.st = Test()
    #     self.hide()
    #     self.st.show()
    #
    # def words(self):
    #     self.st = Words()
    #     self.hide()
    #     self.st.show()
    #
    # def favourites(self):
    #     self.st = Favourites()
    #     self.hide()
    #     self.st.show()
