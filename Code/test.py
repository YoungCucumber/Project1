from constants import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from results import Results

vowels = 'ауоыиэяюёе'


class Test(QMainWindow):
    def __init__(self, db, menu):
        super().__init__()
        uic.loadUi(FILE_TEST, self)
        self.db = db
        self.menu = menu
        self.setWindowTitle(TEST_TITLE)
        self.answers = []
        self.keys = []
        self.cword = 0
        self.btn_apply.clicked.connect(self.run)
        self.run()

    def run(self):
        self.btn_menu.clicked.connect(self.menu_return)
        self.progressbr.setValue(START_PROGRESSBAR)
        self.btngroup = QButtonGroup()
        self.run_functions()

    def run_functions(self):
        if self.spnbox_amount.value() == 0:
            self.set_enabled()
        else:
            self.set_not_enabled()
            self.all_words_list = self.db.random_n_words(self.spnbox_amount.value())
            self.len_all_cards = len(self.all_words_list)
            self.vowels_count()

    def vowels_count(self):
        if self.cword < len(self.all_words_list):
            self.create_variants()
        else:
            self.cword = 0
            self.set_enabled()
            self.lbl_word.setText(LBL_WORD_CHOOSE_AMOUNT)
            self.show_results()
            self.lbl_word.move(150, 200)

    def create_variants(self):
        self.btngroup = QButtonGroup()
        self.main_word, word = self.all_words_list[self.cword][1], list(self.all_words_list[self.cword][1])
        self.lbl_word.setText(self.main_word.lower())
        self.lbl_word.move(320, 200)
        variants = []
        self.keys.append(self.main_word)
        for i, letter in enumerate(word):
            if letter.lower() in vowels:
                variants.append(self.main_word[:i].lower() + letter.upper() + self.main_word[i + 1:].lower())
        self.create_buttons(variants)

    def create_buttons(self, variants):
        self.fill_layout(variants)
        self.btngroup.buttonClicked.connect(self.answer)

    def fill_layout(self, variants):
        for elem in variants:
            self.btn_variant = QPushButton(self)
            self.btn_variant.setText(elem)
            self.btn_variant.setStyleSheet(BTN_ORANGE)
            self.btngroup.addButton(self.btn_variant)
            self.vrtcllayout.addWidget(self.btn_variant)

    def show_results(self):
        self.st = Results(self.answers, self.keys, self)
        self.hide()
        self.st.show()
        self.answers = []
        self.keys = []

    def answer(self, btn):
        self.answers.append(btn.text())
        for i in reversed(range(self.vrtcllayout.count())):
            self.vrtcllayout.itemAt(i).widget().setParent(None)
        self.cword += 1
        self.len_all_cards -= 1
        self.progressbar_change_value()
        self.vowels_count()

    def set_enabled(self):
        self.progressbr.setEnabled(False)
        self.spnbox_amount.setEnabled(True)
        self.btn_apply.setEnabled(True)

    def set_not_enabled(self):
        self.progressbr.setEnabled(True)
        self.spnbox_amount.setEnabled(False)
        self.btn_apply.setEnabled(False)

    def progressbar_change_value(self):
        self.progressbr.setValue(START_PROGRESSBAR * self.len_all_cards / len(self.all_words_list))
        self.spnbox_amount.setValue(self.len_all_cards)

    def menu_return(self):
        self.st = self.menu
        self.hide()
        self.st.show()
