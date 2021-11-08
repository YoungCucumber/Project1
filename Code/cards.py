from constants import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Cards(QMainWindow):
    def __init__(self, db, menu):
        super().__init__()
        uic.loadUi(FILE_CARDS, self)
        self.db = db
        self.menu = menu
        self.setWindowTitle(CARDS_TITLE)
        self.index_current_word = 0
        self.btn_card.clicked.connect(self.change_word)
        self.btn_card_isClicked = False
        self.run_functions()

    def run_functions(self):
        self.btn_apply.clicked.connect(self.run)
        self.btn_next.clicked.connect(self.next_word)
        self.btn_menu.clicked.connect(self.menu_return)
        self.btn_complete.clicked.connect(self.complete)
        self.progressbr.setValue(START_PROGRESSBAR)
        self.run()

    # Считывание данных с SpinBox и создание списка с рандомными слова(длина списка такаяЮ которая указана в SpinBox)
    def run(self):
        if self.spnbox_amount.value() == 0:
            self.set_enabled()
        else:
            self.set_not_enabled()
            self.all_words_list = self.db.random_n_words(self.spnbox_amount.value())
            self.len_all_cards_begin = len(self.all_words_list)
            self.checkbox_is_favourite()
            self.start()

    def start(self):
        self.btn_card_isClicked = False
        if self.index_current_word >= 0:
            self.btn_card.setText(self.all_words_list[self.index_current_word][1].lower())
            self.checkbox_is_favourite()
            self.btn_card.setStyleSheet(BTN_GREY)
        else:
            self.complete()

    # Переворот "карточки" на обратную сторону для показа ответа и наоборот
    def change_word(self):
        if self.btn_card_isClicked:
            self.btn_card.setText(self.all_words_list[self.index_current_word][1].lower())
            self.btn_card.setStyleSheet(BTN_GREY)
            self.lbl_show.setText(SHOW_ANSWERE)
        else:
            self.btn_card.setText(self.all_words_list[self.index_current_word][1])
            self.btn_card.setStyleSheet(BTN_RED)
            self.lbl_show.setText(SHOW_BACK)
        self.btn_card_isClicked = not self.btn_card_isClicked

    # Следующее слово (кнопка "Следующее")
    def next_word(self):
        if self.index_current_word == len(self.all_words_list) - 1:
            self.index_current_word = 0
        else:
            self.index_current_word += 1
        self.start()

    # Удалить слово из списка, чтобы оно больше не появлялось (кнопка "Усвоено")
    def complete(self):
        if len(self.all_words_list) > 0:
            self.all_words_list.remove(self.all_words_list[self.index_current_word])
            self.count_rest_words()
            if self.index_current_word == len(self.all_words_list) - 1:
                self.index_current_word = 0
            if self.index_current_word > len(self.all_words_list) - 1:
                self.index_current_word = 0
        if len(self.all_words_list) == 0:
            self.btn_card.setText(END)
            self.set_enabled()
        else:
            self.start()

    # Сделать так, чтобы было невозможно нажимать на кнопки, когда слова закончатся
    def set_enabled(self):
        self.btn_complete.setEnabled(False)
        self.btn_next.setEnabled(False)
        self.btn_card.setEnabled(False)
        self.progressbr.setEnabled(False)
        self.checkbox_addfavourites.setEnabled(False)
        self.spnbox_amount.setEnabled(True)
        self.btn_apply.setEnabled(True)

    # Сделать так, чтобы пользоватеть не смог изменить данные в SpinBox, а остальные кнопки работали
    def set_not_enabled(self):
        self.btn_complete.setEnabled(True)
        self.btn_next.setEnabled(True)
        self.btn_card.setEnabled(True)
        self.progressbr.setEnabled(True)
        self.checkbox_addfavourites.setEnabled(True)
        self.spnbox_amount.setEnabled(False)
        self.btn_apply.setEnabled(False)

    # Проверка на то, является ли слово избранным
    def checkbox_is_favourite(self):
        favourite_words = self.db.ckeck_is_favourite()
        if len(favourite_words) > 0:
            self.favourite_words_list = favourite_words[0][0].split()
            if self.all_words_list[self.index_current_word][1] in self.favourite_words_list:
                self.checkbox_addfavourites.setChecked(True)
            else:
                self.checkbox_addfavourites.setChecked(False)
            self.checkbox_state_changed()

    # Проверка на изменение состояния чекбокса
    def checkbox_state_changed(self):
        self.checkbox_addfavourites.stateChanged.connect(self.checkbox_add_remove)

    # Узнать, поставил ли пользователь галочку или наоборот убрал и соответственно занести данные в таблицу бд
    def checkbox_add_remove(self):
        if (self.checkbox_addfavourites.isChecked()
                and (self.all_words_list[self.index_current_word][1] not in self.favourite_words_list)):
            self.favourite_words_list.append(self.all_words_list[self.index_current_word][1])
        elif (not self.checkbox_addfavourites.isChecked()
              and (self.all_words_list[self.index_current_word][1] in self.favourite_words_list)):
            self.favourite_words_list.remove(self.all_words_list[self.index_current_word][1])
        self.db.fill_favourites(' '.join(self.favourite_words_list))

    # Подсчет оставшихся слов и отображение этого количества в SpinBox
    def count_rest_words(self):
        self.spnbox_amount.setValue(len(self.all_words_list))
        self.progressbar_change_value()

    # Отображение оставшихся слов в процентах в Progressbar
    def progressbar_change_value(self):
        self.progressbr.setValue(START_PROGRESSBAR * len(self.all_words_list) / self.len_all_cards_begin)

    # Возвращение в меню
    def menu_return(self):
        self.st = self.menu
        self.hide()
        self.st.show()
