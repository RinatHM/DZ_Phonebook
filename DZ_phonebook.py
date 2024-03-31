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
