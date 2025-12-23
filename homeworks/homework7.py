import sqlite3

connect = sqlite3.connect('books.db')
cursor = connect.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        name TEXT NOT NULL,
        author TEXT NOT NULL,
        year TEXT
    )
''')
connect.commit()


# ➕ Добавление книги
def create_book(name, author, year):
    cursor.execute(
        'INSERT INTO books (name, author, year) VALUES (?, ?, ?)',
        (name, author, year)
    )
    connect.commit()
    print(f'Книга добавлена: {name}')


create_book("Евгений Онегин", "Пушкин", "1833")


# 📖 Получение книг
def get_books():
    cursor.execute('SELECT rowid, name, author, year FROM books')
    books = cursor.fetchall()
    for b in books:
        print(f'ID: {b[0]} | Книга: {b[1]} | Автор: {b[2]} | Год: {b[3]}')


get_books()


# ✏ Обновление названия книги
def update_book_name(row_id, new_name):
    cursor.execute(
        'UPDATE books SET name = ? WHERE rowid = ?',
        (new_name, row_id)
    )
    connect.commit()
    print('Книга обновлена!')


update_book_name(1, 'Капитанская дочка')


# 🗑 Удаление книги
def delete_book(row_id):
    cursor.execute(
        'DELETE FROM books WHERE rowid = ?',
        (row_id,)
    )
    connect.commit()
    print('Книга удалена!')


# delete_book(1)
