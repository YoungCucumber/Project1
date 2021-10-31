import random

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Cards(QMainWindow):
    def __init__(self, db, menu):
        super().__init__()
        uic.loadUi('./Designs/cards.ui', self)
        self.db = db
        self.menu = menu
        self.setWindowTitle('Карточки')
        self.index_current_word = 0
        self.btn_apply.clicked.connect(self.run)
        self.btn_next.clicked.connect(self.next_word)
        self.btn_menu.clicked.connect(self.menu_return)
        self.btn_complete.clicked.connect(self.complete)
        self.run()

    def run(self):
        if self.spnbox_amount.value() == 0:
            self.set_enabled()
        else:
            self.set_not_enabled()
            self.all_words_list = self.db.random_n_words(self.spnbox_amount.value())
            self.start()

    def start(self):
        if self.index_current_word >= 0:
            self.btn_card.setText(self.all_words_list[self.index_current_word][1].lower())
            self.btn_card.setStyleSheet("background-color: grey; border: 0.5; font-size: 30px; color: white")
            self.btn_card.clicked.connect(self.change_word)
        else:
            self.complete()

    def change_word(self):
        self.btn_card.setText(self.all_words_list[self.index_current_word][1])
        self.btn_card.setStyleSheet("background-color: red; border: 0.5; font-size: 30px; color: white")
        self.btn_card.clicked.connect(self.start)

    def next_word(self):
        if self.index_current_word == len(self.all_words_list) - 1:
            self.index_current_word = 0
        else:
            self.index_current_word += 1
        self.start()

    def complete(self):
        if len(self.all_words_list) > 0:
            self.all_words_list.remove(self.all_words_list[self.index_current_word])
            if self.index_current_word == len(self.all_words_list) - 1:
                self.index_current_word = 0
            if self.index_current_word > len(self.all_words_list) - 1:
                self.index_current_word = 0
        if len(self.all_words_list) == 0:
            self.btn_card.setText('Слова закончились!')
            self.set_enabled()
        else:
            self.start()

    def set_enabled(self):
        self.btn_complete.setEnabled(False)
        self.btn_next.setEnabled(False)
        self.btn_card.setEnabled(False)
        self.progressbr.setEnabled(False)
        self.checkbox_addfavourites.setEnabled(False)
        self.spnbox_amount.setEnabled(True)
        self.btn_apply.setEnabled(True)

    def set_not_enabled(self):
        self.btn_complete.setEnabled(True)
        self.btn_next.setEnabled(True)
        self.btn_card.setEnabled(True)
        self.progressbr.setEnabled(True)
        self.checkbox_addfavourites.setEnabled(True)
        self.spnbox_amount.setEnabled(False)
        self.btn_apply.setEnabled(False)

    def menu_return(self):
        self.st = self.menu
        self.hide()
        self.st.show()
