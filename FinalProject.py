import sqlite3

def connect():
    return sqlite3.connect('librarysystem.db')

class LibraryManagementSystem:
    def create_tables_(connection):
        cursor = connection.cursor()
        cursor.execute('''
            create table if not exists librarian(
            librarian_id integer primary key autoincrement,
            username text,
            password text,
            name text,
            contact_information text
            )  
            ''')
        cursor.execute('''
            create table if not exists publisher(
            publisher_id integer primary key autoincrement,
            publisher_name text,
            address text,
            contact_details text
            )  
            ''')
        cursor.execute('''
            create table if not exists book(
            book_id integer primary key autoincrement,
            title text,
            author text,
            genre text,
            ISBN integer,
            quantity integer,
            publication_year integer
            )  
            ''')
        cursor.execute('''
            create table if not exists user(
            user_id integer primary key autoincrement,
            username text,
            password text,
            name text,
            contact_information text
            )  
            ''')
        cursor.execute('''
            create table if not exists transaction(
            user_id integer,
            book_id integer,
            due_date date,
            contact_information text,
            foreign key (user_id) references user (user_id),
            foreign key (book_id) references book (book_id),
            foreign key (contact_information) references user (contact_information),
            )  
            ''')
        connection.commit()
        cursor.close()

class Librarian:
    def __init__(self) -> None:
        pass