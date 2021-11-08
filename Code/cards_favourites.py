from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from constants import *


class CardsFavourites(QMainWindow):
    def __init__(self, favourite_words, favourites):
        super().__init__()
        uic.loadUi(FILE_FAVOURITE_CARDS, self)
        self.favourites = favourites
        self.favourite_words = favourite_words
        self.setWindowTitle(FAVOURITE_CARDS_TITLE)
        self.index_current_word = 0
        self.btn_card_isClicked = False
        self.len_words_begin = len(self.favourite_words)
        self.btn_card.clicked.connect(self.change_word)
        self.run()

    def run(self):
        self.btn_next.clicked.connect(self.next_word)
        self.btn_instruction.clicked.connect(self.instruction)
        self.btn_back.clicked.connect(self.favourites_return)
        self.btn_complete.clicked.connect(self.complete)
        self.progressbr.setValue(START_PROGRESSBAR)
        self.start()

    def start(self):
        self.btn_card_isClicked = False
        if self.index_current_word >= 0:
            self.btn_card.setText(self.favourite_words[self.index_current_word].lower())
            self.btn_card.setStyleSheet(BTN_GREY)
        else:
            self.complete()

    # Переворот "карточки" на обратную сторону для показа ответа и наоборот
    def change_word(self):
        if self.btn_card_isClicked:
            self.btn_card.setText(self.favourite_words[self.index_current_word].lower())
            self.btn_card.setStyleSheet(BTN_GREY)
            self.lbl_show.setText(SHOW_ANSWERE)
        else:
            self.btn_card.setText(self.favourite_words[self.index_current_word])
            self.btn_card.setStyleSheet(BTN_RED)
            self.lbl_show.setText(SHOW_BACK)
        self.btn_card_isClicked = not self.btn_card_isClicked

    # Удалить слово из списка, чтобы оно больше не появлялось (кнопка "Усвоено")
    def complete(self):
        if len(self.favourite_words) > 0:
            self.favourite_words.remove(self.favourite_words[self.index_current_word])
            self.progressbar_change_value()
            if self.index_current_word == len(self.favourite_words) - 1:
                self.index_current_word = 0
            if self.index_current_word > len(self.favourite_words) - 1:
                self.index_current_word = 0
        if len(self.favourite_words) == 0:
            self.btn_card.setText(END)
            self.set_enabled()
        else:
            self.start()

    # Следующее слово (кнопка "Следующее")
    def next_word(self):
        if self.index_current_word == len(self.favourite_words) - 1:
            self.index_current_word = 0
        else:
            self.index_current_word += 1
        self.start()

    # Message box
    def instruction(self):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle(MSGBOX_TITLE)
        msgbox.setText(INSTRUCTION_FAVOURITES_CARDS)
        msgbox.setStandardButtons(QMessageBox.Ok)
        exit_value = msgbox.exec()

    # Отображение оставшихся слов в процентах в Progressbar
    def progressbar_change_value(self):
        self.progressbr.setValue(START_PROGRESSBAR * len(self.favourite_words) / self.len_words_begin)

    # Сделать так, чтобы пользоватеть не смог изменить данные в SpinBox, а остальные кнопки работали
    def set_enabled(self):
        self.btn_card.setEnabled(False)
        self.btn_complete.setEnabled(False)
        self.btn_next.setEnabled(False)

    # Вернуться к избранным словам
    def favourites_return(self):
        self.st = self.favourites
        self.hide()
        self.st.show()
