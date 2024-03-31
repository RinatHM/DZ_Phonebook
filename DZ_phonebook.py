import sqlite3 as sl
from  easygui import *

# функция добавления номера
def add_values():
    cur.execute("INSERT INTO users (name, surname, number_phone, birthday) VALUES (?, ?, ?, ?)", (sql_name, sql_surname, sql_number_phone, sql_birthday))
#функция изменения  номера
def change_values():
    cur.execute("UPDATE users SET  number_phone = ? WHERE name = ? and surname = ?", (sql_number_phone, sql_name, sql_surname ))
#функция поиска  номера
def find_values():
    cur.execute("SELECT * FROM users WHERE name = ?", (sql_name, ))
#функция удаления  номера
def del_values():
    cur.execute("DELETE FROM users WHERE name = ? AND surname = ?", (sql_name, sql_surname))

# создаём переменные для каждого столбца таблицы справочника
sql_request = ''
sql_values = ''
sql_name = ''
sql_surname = ''
sql_number_phone = ''
sql_birthday = ''

#создаём подключение к БД
conn = sl.connect('tel_sprav.db')
# #создаём курсор - объект для выполнения SQL
cur = conn.cursor()

# #создали SQL запрос и выполнили
cur.execute("""
            CREATE TABLE IF NOT EXISTS users
            (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            number_phone TEXT,
            birthday TEXT
            );
            """)

while True: # запуск программы
    cur.execute("SELECT * from users;")
   # print(cur.fetchall()) # входим и
    for i in cur.fetchall():
            print(i)
    command=input("Введите команду ")
    if command =="/change":
        sql_name = input("Введите имя ")
        sql_surname = input("Введите фамилию ")
        sql_number_phone = input("Введите новый номер ")
        change_values()
        cur.execute("SELECT * from users;")
        for i in cur.fetchall():
            print(i)
        break
    if command =="/add":
        sql_name = input("Введите имя ")
        sql_surname = input("Введите фамилию ")
        sql_number_phone = input("Введите новый номер ")
        sql_birthday = input("Введите дату рождения")
        add_values()
        cur.execute("SELECT * from users;")
        for i in cur.fetchall():
            print(i)
        break
    if command =="/find":
        sql_name = input("Введите имя ")
        find_values()
        print(*cur.fetchall()) #
        break
    if command =="/del":
        sql_name = input("Введите имя ")
        sql_surname = input("Введите фамилию ")
        del_values()
        print(f"Номер под именем {sql_name} {sql_surname} удалён")
        print(*cur.fetchall()) # входим и просматриваем справочник
        break

conn.commit()