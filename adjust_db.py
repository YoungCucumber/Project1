import sqlite3
from random import shuffle


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect('EGEstresses.db')
        self.cur = self.con.cursor()
        self.count_users = 0
        self.fill_list_of_words_table()

    def fill_list_of_words_table(self):
        file = open('words.txt').readlines()
        for i, line in enumerate(file):
            line = line.strip()
            self.cur.execute("""INSERT or REPLACE INTO list_of_words VALUES (?, ?)""", (i + 1, line)).fetchone()
            self.con.commit()

    def fill_user_table(self, login, password):
        self.count_users += 1
        # self.cur.execute("""INSERT INTO Users VALUES(?, ?, ?, ?)""", (self.count_users, login, password, '')).fetchall()
        self.cur.execute("""INSERT INTO users(login, password, favourites)
                    VALUES(?, ?, ?)""", (login, password, '')).fetchall()
        self.con.commit()
        for i in self.cur.execute("""SELECT * FROM Users"""):
            print(i)

    def check_right_password(self, password, login):
        data_about_user = self.cur.execute("""SELECT * FROM Users WHERE login=? """, (login,)).fetchone()
        if password == data_about_user[2]:
            return True

    def check_login_exist(self, login):
        data_login = self.cur.execute("""SELECT login FROM Users WHERE login=?""", (login,)).fetchone()
        if data_login:
            return True
        else:
            return False

    def check_exist_login_registration(self, login):
        data_login = self.cur.execute("""SELECT login FROM Users WHERE login=?""", (login,)).fetchone()
        if data_login:
            return True
        else:
            return False

    def random_n_words(self, n):
        words = self.cur.execute("""SELECT * FROM list_of_words""").fetchall()
        shuffle(words)
        return words[:n]
