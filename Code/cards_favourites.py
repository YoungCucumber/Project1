# import random
#
# from PyQt5 import uic, QtWidgets
# from constants import *
# from PyQt5.QtWidgets import QApplication, QMainWindow
#
# class Favourites(QMainWindow):
#     def __init__(self, db, menu):
#         super().__init__()
#         self.menu = menu
#         self.db = db
#         uic.loadUi(FILE_FAVOURITE_CARDS, self)
#         self.setWindowTitle(WORDS_TITLE)
#         self.favourite_words = []
#         self.list_of_checkboxes = []
#         self.adjust_image()
#         self.run()