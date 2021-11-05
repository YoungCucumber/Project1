# from PyQt5 import uic, QtWidgets
# from constants import *
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
#
# class CardsFavourites(QMainWindow):
#     def __init__(self, favourite_words, favourites):
#         super().__init__()
#         self.favourites = favourites
#         self.favourite_words = favourite_words
#         uic.loadUi(FILE_FAVOURITE_CARDS, self)
#         self.setWindowTitle(FAVOURITE_CARDS_TITLE)
#         self.count = 0
#         self.run()
#
#     def run(self):
#         self.btn_instruction.clicked.connect(self.instruction)
#         # self.btn_next.clicked.connect(self.next_word)
#         self.btn_back.clicked.connect(self.favourites_return)
#         self.btn_card.setText(self.favourite_words[0].lower())
#         # self.btn_complete.clicked.connect(self.complete)
#         self.start()
#
#     def start(self):
#         for i in range(len(self.favourite_words)):
#             if self.count == 0:
#                 self.btn_card.clicked.connect(lambda: self.change_red(i))
#                 self.btn_next.clicked.connect(lambda: self.next_word(i))
#                 self.btn_complete.clicked.connect(lambda: self.complete(i))
#             elif self.count == 1:
#                 self.btn_card.clicked.connect(lambda: self.change_grey(i))
#                 self.btn_next.clicked.connect(lambda: self.next_word(i))
#                 self.btn_complete.clicked.connect(lambda: self.complete(i))
#
#     def change_red(self, i):
#         self.btn_card.setText(self.favourite_words[i].lower())
#         self.btn_card.setStyleSheet(BTN_RED)
#         self.count = 1
#
#     def change_grey(self, i):
#         self.btn_card.setText(self.favourite_words[i])
#         self.btn_card.setStyleSheet(BTN_GREY)
#         self.count = 0
#
#     def next_word(self, i):
#         i += 1
#
#     def complete(self, i):
#         self.favourite_words.remove(self.favourite_words[i])
#
#     def instruction(self):
#         msgbox = QMessageBox()
#         msgbox.setIcon(QMessageBox.Information)
#         msgbox.setWindowTitle(MSGBOX_TITLE)
#         msgbox.setText(INSTRUCTION_FAVOURITES_CARDS)
#         msgbox.setStandardButtons(QMessageBox.Ok)
#         exit_value = msgbox.exec()
#
#     def favourites_return(self):
#         self.st = self.favourites
#         self.hide()
#         self.st.show()
#
#
