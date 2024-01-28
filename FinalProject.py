import sqlite3

def connect():
    return sqlite3.connect('librarysystem.db')

class LibraryManagementSystem:
    def create_tables(self,connection):
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
    def __init__(self, connection):
        self.connection = connection

    def add_librarian(self,username,password,name,contact_information):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO librarian (username, password, name, contact_information) VALUES (?, ?, ?, ?)',
                       (username, password, name, contact_information))
        self.connection.commit()
        
    def edit_librarian(self,new_password,new_contact_information,username):
        cursor = self.connection.cursor()
        if new_password:
            cursor.execute('UPDATE librarian SET password = ? WHERE username = ?',
                       (new_password,username))
        elif new_contact_information:
            cursor.execute('UPDATE librarian SET contact_information = ? WHERE username = ?',
                       (new_contact_information,username))
        self.connection.commit()

    def delete_librarian(self,username):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM librarian WHERE username = ?',
                       (username,))
        self.connection.commit()

class Publisher:
    def __init__(self, connection):
        self.connection = connection

    def add_publisher(self,publisher_name,address,contact_details):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO publisher (publisher_name,address,contact_details) VALUES (?, ?, ?)',
                       (publisher_name,address,contact_details))
        self.connection.commit()
        
    def edit_publisher(self,publisher_name,new_address,new_contact_details):
        cursor = self.connection.cursor()
        if new_address:
            cursor.execute('UPDATE publisher SET address = ? WHERE publisher_name = ?',
                       (new_address,publisher_name))
        elif new_contact_details:
            cursor.execute('UPDATE publisher SET contact_details = ? WHERE publisher_name = ?',
                       (new_contact_details,publisher_name))
        self.connection.commit()

    def delete_publisher(self,publisher_name):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM publisher WHERE publisher_name = ?',
                       (publisher_name,))
        self.connection.commit()

class Book:
    def __init__(self, connection):
        self.connection = connection

    def add_book(self,title,author,genre,ISBN,quantity,publication_year):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO book (title,author,genre,ISBN,quantity,publication_year) VALUES (?, ?, ?, ?, ?, ?)',
                       (title,author,genre,ISBN,quantity,publication_year))
        self.connection.commit()
        
    def edit_book(self,new_title,new_author,new_genre,new_ISBN,new_quantity,new_publication_year,book_id):
        cursor = self.connection.cursor()
        if new_title:
            cursor.execute('UPDATE publisher SET title = ? WHERE book_id = ?',
                       (new_title,book_id))
        elif new_author:
            cursor.execute('UPDATE publisher SET author = ? WHERE book_id = ?',
                       (new_author,book_id))
        elif new_genre:
            cursor.execute('UPDATE publisher SET genre = ? WHERE book_id = ?',
                       (new_genre,book_id))
        elif new_ISBN:
            cursor.execute('UPDATE publisher SET ISBN = ? WHERE book_id = ?',
                       (new_ISBN,book_id))
        elif new_quantity:
            cursor.execute('UPDATE publisher SET quantity = ? WHERE book_id = ?',
                       (new_quantity,book_id))
        elif new_publication_year:
            cursor.execute('UPDATE publisher SET publication_year = ? WHERE book_id = ?',
                       (new_publication_year,book_id))  
        self.connection.commit()
        

    def delete_book(self,book_id):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM book WHERE book_id = ?',
                       (book_id,))
        self.connection.commit()


