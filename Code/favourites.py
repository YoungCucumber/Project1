from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from constants import *
from cards_favourites import CardsFavourites

from PIL import Image


class Favourites(QMainWindow):
    def __init__(self, db, menu):
        super().__init__()
        uic.loadUi(FILE_WORDS, self)
        self.menu = menu
        self.db = db
        self.setWindowTitle(FAVOURITES_TITLE)
        self.favourite_words = []
        self.list_of_checkboxes = []
        self.adjust_image()
        self.run()


    # Для сжатия логотипа программы, потому что он не помещается в отведенное ему пространство в дизайнере
    def adjust_image(self):
        im = Image.open(IMAGE)
        width = 300
        height = 100
        im2 = im.resize((width, height))
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

    # заполнение Layout чекбоксами
    def fill_formlayout(self):
        self.fill_list_of_checkboxes()
        # расстановка чекбоксов, если их нечетное количество
        if len(self.list_of_checkboxes) % 2 == 1:
            for j in range(0, len(self.list_of_checkboxes) - 1, 2):
                self.formlyt.addRow(self.list_of_checkboxes[j], self.list_of_checkboxes[j + 1])
            self.formlyt.addRow((self.list_of_checkboxes[-1]))
        else:
            # расстановка чекбоксов, если их четное количество
            for j in range(0, len(self.list_of_checkboxes) - 1, 2):
                self.formlyt.addRow(self.list_of_checkboxes[j], self.list_of_checkboxes[j + 1])

    # Создание списка с чекбоксами, на которых написаны слова
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

    # Message box
    def instruction(self):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle(MSGBOX_TITLE)
        msgbox.setText(INSTRUCTION_FAVOURITES)
        msgbox.setStandardButtons(QMessageBox.Ok)
        exit_value = msgbox.exec()

    # Создание кнопки "Заучивание" (я использовала тот же файл с дизайном в этом окне, что и для окна "Все слова"
    # Поэтому необходимо создать кнопку вручную
    def create_button(self):
        self.btn_cards_favourites = QPushButton(self)
        self.btn_cards_favourites.move(410, 0)
        self.btn_cards_favourites.resize(191, 61)
        self.btn_cards_favourites.setStyleSheet(BTN_CARDS_FAVOURITE_STYLE)
        self.btn_cards_favourites.setText(BTN_CARDS_FAVOURITE_TEXT)
        if len(self.list_of_checkboxes) == 0:
            self.btn_cards_favourites.setEnabled(False)
        self.btn_cards_favourites.clicked.connect(self.open_cards_favourites)

    # Возвращение в меню и добавление всех слов, отмеченных галочкой в избранные(обновление таблицы Favourites)
    def menu_return(self):
        self.save_favourites()
        self.db.fill_favourites(' '.join(self.favourite_words))
        self.st = self.menu
        self.hide()
        self.st.show()

    # Создание списка с избранными словами (тк человек мог убрать некоторые слова из этого списка,\
    # убрав галочку с чекбокса)
    def save_favourites(self):
        for i in self.list_of_checkboxes:
            if i.isChecked():
                self.favourite_words.append(i.text())

    # Открытие окна "Заучивание избранных слов"
    def open_cards_favourites(self):
        self.save_favourites()
        self.st = CardsFavourites(self.favourite_words, self)
        self.hide()
        self.st.show()
