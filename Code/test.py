from constants import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

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
        self.run()

    def run(self):
        self.btn_apply.clicked.connect(self.run)
        self.btn_menu.clicked.connect(self.menu_return)
        self.progressbr.setValue(START_STATUSBAR)
        self.btngroup = QButtonGroup()
        self.run_functions()

    def run_functions(self):
        if self.spnbox_amount.value() == 0:
            self.set_enabled()
        else:
            self.set_not_enabled()
            self.all_words_list = self.db.random_n_words(self.spnbox_amount.value())
            self.len_all_cards_begin = len(self.all_words_list)
            self.vowels_count()

    def vowels_count(self):
        for word in self.all_words_list:
            variants = []
            self.question_word = word[1]
            self.keys.append(self.question_word)
            word = list(word[1])
            for i, letter in enumerate(word):
                if letter.lower() in vowels:
                    variants.append(self.question_word[:i].lower() + letter.upper() + self.question_word[i + 1:].lower())
            self.fill_layout(variants)
            self.btngroup.buttonClicked.connect(self.answer)

    def fill_layout(self, variants):
        for elem in variants:
            self.btn_variant = QPushButton(self)
            self.btn_variant.setText(elem)
            self.btn_variant.setStyleSheet(BTN_ORANGE)
            self.btngroup.addButton(self.btn_variant)
            self.vrtcllayout.addWidget(self.btn_variant)

    def answer(self, btn):
        self.answers.append(btn.text())
        for i in reversed(range(self.vrtcllayout.count())):
            self.vrtcllayout.itemAt(i).widget().setParent(None)
        print(self.answers)

    def set_enabled(self):
        self.progressbr.setEnabled(False)
        self.spnbox_amount.setEnabled(True)
        self.btn_apply.setEnabled(True)

    def set_not_enabled(self):
        self.progressbr.setEnabled(True)
        self.spnbox_amount.setEnabled(False)
        self.btn_apply.setEnabled(False)

    def menu_return(self):
        self.st = self.menu
        self.hide()
        self.st.show()