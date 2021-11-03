from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from constants import *
from PIL import Image



class Favourites(QMainWindow):
    def __init__(self, db, menu):
        super().__init__()
        self.menu = menu
        self.db = db
        uic.loadUi(FILE_WORDS, self)
        self.setWindowTitle(WORDS_TITLE)
        self.favourite_words = []
        self.list_of_checkboxes = []
        self.adjust_image()
        self.run()

    def adjust_image(self):
        im = Image.open(IMAGE)
        im2 = im.resize(NEW_SIZE_IMAGE)
        im2.save(IMAGE_RESIZED)

    def run(self):
        self.btn_menu.clicked.connect(self.menu_return)
        self.btn_instruction.clicked.connect(self.instruction)
        self.formlyt = QFormLayout()
        self.widget = QWidget()
        self.fill_formlayout()
        self.formlyt.setHorizontalSpacing(SPACE_BETWEEN_COLUMNS)
        self.widget.setLayout(self.formlyt)
        self.scrlarea_words.setWidget(self.widget)
        self.create_button()

    def fill_formlayout(self):
        self.fill_list_of_checkboxes()
        if len(self.list_of_checkboxes) % 2 == 1:
            for j in range(0, len(self.list_of_checkboxes) - 1, 2):
                self.formlyt.addRow(self.list_of_checkboxes[j], self.list_of_checkboxes[j + 1])
            self.formlyt.addRow((self.list_of_checkboxes[-1]))
        else:
            for j in range(0, len(self.list_of_checkboxes) - 1, 2):
                self.formlyt.addRow(self.list_of_checkboxes[j], self.list_of_checkboxes[j + 1])

    def fill_list_of_checkboxes(self):
        self.is_favourite = self.db.ckeck_is_favourite()
        if len(self.is_favourite) > 0:
            self.is_favourite = self.is_favourite[0][0].split()
            for i in self.is_favourite:
                self.checkbox = QCheckBox(self)
                self.checkbox.setText(i)
                self.checkbox.setStyleSheet(FONT_CHECKBOX)
                self.checkbox.setChecked(True)
                self.list_of_checkboxes.append(self.checkbox)

    def instruction(self):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle(MSGBOX_TITLE)
        msgbox.setText(INSTRUCTION_FAVOURITES)
        msgbox.setStandardButtons(QMessageBox.Ok)
        exit_value = msgbox.exec()

    def create_button(self):
        self.btn_cards_favourites = QPushButton(self)
        self.btn_cards_favourites.move(410, 0)
        self.btn_cards_favourites.resize(191, 61)
        self.btn_cards_favourites.setStyleSheet(BTN_CARDS_FAVOURITE_STYLE)
        self.btn_cards_favourites.setText(BTN_CARDS_FAVOURITE_TEXT)
        self.btn_cards_favourites.clicked.connect(self.open_cards_favourites)

    def menu_return(self):
        for i in self.list_of_checkboxes:
            if i.isChecked():
                self.favourite_words.append(i.text())
        self.db.fill_favourites(' '.join(self.favourite_words))
        self.st = self.menu
        self.hide()
        self.st.show()