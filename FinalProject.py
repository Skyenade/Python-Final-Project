import sqlite3

def connect():
    return sqlite3.connect('librarysystem.db')

class LibraryManagementSystem:
    def create_tables_(connection):
        cursor = connection.cursor()
        cursor.execute('''
            create table if not exists librarians(
            username text not null,
            password text,
            name text,
            contact_information text
            )  
            ''')
        cursor.execute('''
            create table if not exists publisher(
            publisher_name text,
            address text,
            contact_information text
            )  
            ''')
        cursor.execute('''
            create table if not exists users(
            id integer primary key autoincrement,
            name text not null,
            age integer
            )  
            ''')
        cursor.execute('''
            create table if not exists users(
            id integer primary key autoincrement,
            name text not null,
            age integer
            )  
            ''')
        connection.commit()
        cursor.close()