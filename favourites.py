# from PyQt5 import uic, QtWidgets, QtGui
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
#
#
#
# class Words(QMainWindow):
#     def __init__(self, db, menu):
#         super().__init__()
#         self.menu = menu
#         self.db = db
#         uic.loadUi('./Designs/words.ui', self)
#         self.setWindowTitle('Избранное')
#         self.favourite_words = []
#         self.list_of_checkboxes = []
#         self.run()
#
#     def run(self):
#         self.btn_menu.clicked.connect(self.menu_return)
#         self.formlyt = QFormLayout()
#         self.widget = QWidget()
#         self.fill_formlayout()
#         self.formlyt.setHorizontalSpacing(320)
#         self.widget.setLayout(self.formlyt)
#         self.scrlarea_words.setWidget(self.widget)
#
#     def fill_formlayout(self):
#         for i in range(476):
#             self.checkbox = QCheckBox(self)
#             self.checkbox.setText(self.db.word_by_id(i)[0])
#             self.list_of_checkboxes.append(self.checkbox)
#         for j in range(0, 476, 2):
#             self.formlyt.addRow(self.list_of_checkboxes[j], self.list_of_checkboxes[j + 1])
#
#     def menu_return(self):
#         for i in self.list_of_checkboxes:
#             if i.isChecked():
#                 self.favourite_words.append(i.text())
#         self.db.fill_favourites(' '.join(self.favourite_words))
#         self.st = self.menu
#         self.hide()
#         self.st.show()