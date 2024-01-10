from .database_connection import DatabaseConnection
from typing import List,Dict
#cursor->All operation in sqllite are made by cursor , and not by the connection object itself

#That is so that we can have one single connection , but potentially multiple cirsor either reading data and at most one writing data.
#commit->save the bunch of this query to disk and keep a bunch of data in memory until we commit



def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary Key,author text,read integer)')

def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM books')
        books=[{'name':row[0],'author':row[1],'read':row[2]} for row in cursor.fetchall() ]
        return books
def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()
    #cursor.execute(f'INSERT INTO books VALUES("{name}","{author}",0)')
        cursor.execute(f'INSERT INTO books VALUES(?,?,0)',(name,author))
        connection.commit()
        connection.close()

def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))
        connection.commit()
        connection.close()


def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE books SET FROM WHERE name=?', (name,))
        connection.commit()
        connection.close()
