import sqlite3
from random import shuffle


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect('EGEstresses.db')
        self.cur = self.con.cursor()
        self.count_users = 0
        self.fill_list_of_words_table()
        self.current_user = None

    def fill_list_of_words_table(self):
        file = open('words.txt', encoding='utf-8').readlines()
        for i, line in enumerate(file):
            line = line.strip()
            self.cur.execute("""INSERT or REPLACE INTO list_of_words VALUES (?, ?)""", (i, line)).fetchone()
            self.con.commit()

    def fill_user_table(self, login, password):
        id_previous = self.cur.execute("""SELECT * FROM Users""").fetchall()[-1][0]
        self.cur.execute("""INSERT INTO users(login, password, favourite)
                    VALUES(?, ?, ?)""", (login, password, id_previous + 1)).fetchall()
        self.con.commit()
        self.current_user = id_previous + 1

    def check_right_password(self, password, login):
        data_about_user = self.cur.execute("""SELECT * FROM Users WHERE login=? """, (login,)).fetchone()
        if password == data_about_user[2]:
            self.current_user = data_about_user[0]
            return True

    def check_login_exist(self, login):
        data_login = self.cur.execute("""SELECT login FROM Users WHERE login=?""", (login,)).fetchone()
        if data_login:
            return True
        else:
            return False

    def random_n_words(self, n):
        words = self.cur.execute("""SELECT * FROM list_of_words""").fetchall()
        shuffle(words)
        return words[:n]

    def word_by_id(self, i):
        return self.cur.execute("""SELECT word FROM list_of_words WHERE id=?""", (i,)).fetchone()

    def fill_favourites(self, favourite_words):
        self.cur.execute("""INSERT or REPLACE INTO Favourites VALUES(?, ?)""", (self.current_user, favourite_words))
        self.con.commit()

    def ckeck_is_favourite(self):
        favourites_string = (self.cur.execute("""SELECT word FROM Favourites 
        WHERE id=?""", (self.current_user,)).fetchall())
        return favourites_string