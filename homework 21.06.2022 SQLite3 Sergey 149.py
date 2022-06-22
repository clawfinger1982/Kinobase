# 1.Сформулируйте SQL запрос для создания таблицы movies.
# Поля: movie_id, name TEXT, release_year INTEGER, genre TEXT
# 2. Создать функции:
# 1. Добавить фильм (заполнение делать с клавиатуры)
# 2. Получения данных обо всех фильмах
# 3. Получения данных об одном фильме по id
# 0. Выход
# 3. Функции вызывать в цикле, чтоб у пользователя был выбор.
import sqlite3
conn = sqlite3.connect('m_name.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, release INTEGER, genre TEXT)''')
conn.commit()
cursor.execute('''SELECT*FROM movies''')
k = cursor.fetchall()
# print('First info', k)

while True:
    a = input('Введите действие '
              '(1 - Добавить фильм, '
              '2 - Получение данных обо всех фильмах, '
              '3 - получение данных об одном фильме по id, 1 из '
             '0 - Выход): ')
    def addfilm():
        name = input('name: ')
        release = int(input('year: '))
        genre = input('genre: ')
        cursor.execute('''INSERT INTO movies(name,release,genre) VALUES (?,?,?)''', (name, release, genre))
        conn.commit()
        cursor.execute('''SELECT*FROM movies''')
        k = cursor.fetchall()
        # return print('Info', k)

    def allinfo():
        conn.commit()
        cursor.execute('''SELECT*FROM movies''')
        k = cursor.fetchall()
        return print('allinfo', k)

    def idinfo():
        movie_id=input('input id: ')
        cursor.execute('''SELECT*FROM movies WHERE id=?''', (movie_id))
        k = cursor.fetchall()
        return print('idinfo', k)

    if a == '1':
        # print('1')
        addfilm()
        continue
    elif a == '2':
        # print('2')
        allinfo()
        continue
    elif a == '3':
        # print('3')
        idinfo()
        continue
    else:
        print('exit')
        break




