from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from constants import *

from PIL import Image


class Words(QMainWindow):
    def __init__(self, db, menu):
        super().__init__()
        uic.loadUi(FILE_WORDS, self)
        self.menu = menu
        self.db = db
        self.setWindowTitle(WORDS_TITLE)
        self.favourite_words = []
        self.list_of_checkboxes = []
        self.adjust_image()
        self.run()
        self.adjust_image()

    # Для сжатия логотипа программы, потому что он не помещается в отведенное ему пространство в дизайнере
    def adjust_image(self):
        im = Image.open(IMAGE)
        width = 300
        height = 100
        im2 = im.resize((width, height))
        im2.save(IMAGE_RESIZED)
        self.pixmax = QPixmap(IMAGE_RESIZED)
        self.lbl_logo.setPixmap(self.pixmax)

    def run(self):
        self.btn_menu.clicked.connect(self.menu_return)
        self.btn_instruction.clicked.connect(self.instruction)
        self.formlyt = QFormLayout()
        self.widget = QWidget()
        self.fill_formlayout()
        self.formlyt.setHorizontalSpacing(SPACE_BETWEEN_COLUMNS)
        self.widget.setLayout(self.formlyt)
        self.scrlarea_words.setWidget(self.widget)

    # заполнение Layout чекбоксами
    def fill_formlayout(self):
        self.fill_list_of_checkboxes()
        for j in range(0, ALL_WORDS_AMOUNT, 2):
            self.formlyt.addRow(self.list_of_checkboxes[j], self.list_of_checkboxes[j + 1])

    # Создание списка с чекбоксами, на которых написаны слова
    def fill_list_of_checkboxes(self):
        self.is_favourite = self.db.ckeck_is_favourite()
        if len(self.is_favourite) > 0:
            self.is_favourite = self.is_favourite[0][0].split()
        for i in range(ALL_WORDS_AMOUNT):
            self.checkbox = QCheckBox(self)
            self.text = self.db.word_by_id(i)[0]
            self.checkbox.setText(self.text)
            self.checkbox.setStyleSheet(FONT_CHECKBOX)
            if len(self.is_favourite) > 0:
                self.set_checked()
            self.list_of_checkboxes.append(self.checkbox)

    # Проверка, является ли слово избранным. Если да, то отметить его галочкой
    def set_checked(self):
        if self.text in self.is_favourite:
            self.checkbox.setChecked(True)

    # Message Box
    def instruction(self):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle(MSGBOX_TITLE)
        msgbox.setText(INSTRUCTION)
        msgbox.setStandardButtons(QMessageBox.Ok)
        exit_value = msgbox.exec()

    # Возвращение в меню и добавление всех слов, отмеченных галочкой в избранные(обновление таблицы Favourites)
    def menu_return(self):
        for checkbox in self.list_of_checkboxes:
            if checkbox.isChecked():
                self.favourite_words.append(checkbox.text())
        self.db.fill_favourites(' '.join(self.favourite_words))
        self.st = self.menu
        self.hide()
        self.st.show()
