import sqlite3
from random import shuffle

from constants import *


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect(DATA_BASE)
        self.cur = self.con.cursor()
        self.count_users = 0
        self.fill_list_of_words_table()
        self.current_user = None

    def fill_list_of_words_table(self):
        file = open(FILE_WITH_ALL_WORDS, encoding='utf-8').readlines()
        for i, line in enumerate(file):
            line = line.strip()
            value = f"""INSERT or REPLACE INTO {LIST_OF_WORDS} VALUES (?, ?)"""
            self.cur.execute(value, (i, line)).fetchone()
            self.con.commit()

    def fill_user_table(self, login, password):
        value = f"""SELECT * FROM {USERS}"""
        id_previous = self.cur.execute(value).fetchall()[-1][0]
        value = f"""INSERT INTO {USERS} (login, password, favourite) VALUES(?, ?, ?)"""
        self.cur.execute(value, (str(login), str(password), id_previous + 1)).fetchall()
        self.con.commit()
        self.current_user = id_previous + 1

    def check_right_password(self, password, login):
        value = f"""SELECT * FROM {USERS} WHERE {LOGIN}=? """
        data_about_user = self.cur.execute(value, (login,)).fetchone()
        if str(password) == str(data_about_user[2]):
            self.current_user = data_about_user[0]
            return True

    def check_login_exist(self, login):
        value = f"""SELECT {LOGIN} FROM {USERS} WHERE {LOGIN}=?"""
        data_login = self.cur.execute(value, (login,)).fetchone()
        if data_login:
            return True
        else:
            return False

    def random_n_words(self, n):
        value = f"""SELECT * FROM {LIST_OF_WORDS}"""
        words = self.cur.execute(value).fetchall()
        shuffle(words)
        return words[:n]

    def word_by_id(self, i):
        value = f"""SELECT {WORD} FROM {LIST_OF_WORDS} WHERE {ID}=?"""
        return self.cur.execute(value, (i,)).fetchone()

    def fill_favourites(self, favourite_words):
        value = f"""INSERT or REPLACE INTO {FAVOURITES} VALUES(?, ?)"""
        self.cur.execute(value, (self.current_user, favourite_words))
        self.con.commit()

    def ckeck_is_favourite(self):
        value = f"""SELECT word FROM {FAVOURITES} WHERE {ID}=?"""
        favourites_string = (self.cur.execute(value, (self.current_user,)).fetchall())
        return favourites_string