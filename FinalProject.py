import sqlite3
from collections import namedtuple, defaultdict


class LibraryManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect('librarysystem.db')
        self.cursor = self.conn.cursor()

        self.create_tables()

        self.librarians_list = []
        self.publishers_list = []
        self.books_list = []
        self.users_list = []
        self.transactions_tuple = ()
    
    def create_tables(self,connection):
        cursor = connection.cursor()
        cursor.execute('''
            create table if not exists librarian(
            username text primary key,
            password text,
            name text,
            contact_information text
            )  
            ''')
        cursor.execute('''
            create table if not exists publisher(
            publisher_name text primary key,
            address text,
            contact_details text
            )  
            ''')
        cursor.execute('''
            create table if not exists book(
            title text,
            author text,
            genre text,
            ISBN integer primary key,
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
            transaction_id primary key autoincrement,
            user_id integer,
            book_id integer,
            due_date date,
            status text,
            foreign key (user_id) references user (user_id),
            foreign key (book_id) references book (book_id),
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
            LibraryManagementSystem.librarians_list.append(self.username, self.password, self.name, self.contact_info)
            self.connection.commit()
            
        def edit_librarian(self,username,new_password,new_name,new_contact_information):
            cursor = self.connection.cursor()

            if new_password:
                cursor.execute('UPDATE librarian SET password = ? WHERE username = ?',
                        (new_password,username))
                
                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == username:
                        librarian_data = (librarian_data[0], new_password, librarian_data[2], librarian_data[3])

            elif new_contact_information:
                cursor.execute('UPDATE librarian SET contact_information = ? WHERE username = ?',
                        (new_contact_information,username))
                
                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == new_contact_information:
                        librarian_data = (librarian_data[0], librarian_data[1], librarian_data[2], new_contact_information)

            elif new_name:
                cursor.execute('UPDATE librarian SET username = ? WHERE username = ?',
                        (new_name,username))
                
                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == new_name:
                        librarian_data = (librarian_data[0], librarian_data[1], new_name, librarian_data[3])
            
            self.connection.commit()

        def delete_librarian(self,username):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM librarian WHERE username = ?',
                        (username,))
            
            for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == username:
                        librarian_data = (librarian_data[0], new_password, librarian_data[2], librarian_data[3])
            self.connection.commit()

    class Publisher:
        def __init__(self, connection):
            self.connection = connection

        def add_publisher(self,publisher_name,address,contact_details):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO publisher (publisher_name,address,contact_details) VALUES (?, ?, ?)',
                        (publisher_name,address,contact_details))
            self.connection.commit()
            
        def edit_publisher(self,new_publisher_name,new_address,new_contact_details,publisher_id):
            cursor = self.connection.cursor()
            if new_address:
                cursor.execute('UPDATE publisher SET address = ? WHERE publisher_id = ?',
                        (new_address,publisher_id))
            elif new_contact_details:
                cursor.execute('UPDATE publisher SET contact_details = ? WHERE publisher_id = ?',
                        (new_contact_details,publisher_id))
            elif new_publisher_name:
                cursor.execute('UPDATE publisher SET publisher_name = ? WHERE publisher_id = ?',
                        (new_publisher_name,publisher_id))
            self.connection.commit()

        def delete_publisher(self,publisher_id):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM publisher WHERE publisher_id = ?',
                        (publisher_id,))
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
                cursor.execute('UPDATE book SET title = ? WHERE book_id = ?',
                        (new_title,book_id))
            elif new_author:
                cursor.execute('UPDATE book SET author = ? WHERE book_id = ?',
                        (new_author,book_id))
            elif new_genre:
                cursor.execute('UPDATE book SET genre = ? WHERE book_id = ?',
                        (new_genre,book_id))
            elif new_ISBN:
                cursor.execute('UPDATE book SET ISBN = ? WHERE book_id = ?',
                        (new_ISBN,book_id))
            elif new_quantity:
                cursor.execute('UPDATE book SET quantity = ? WHERE book_id = ?',
                        (new_quantity,book_id))
            elif new_publication_year:
                cursor.execute('UPDATE book SET publication_year = ? WHERE book_id = ?',
                        (new_publication_year,book_id))  
            self.connection.commit()
            

        def delete_book(self,book_id):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM book WHERE book_id = ?',
                        (book_id,))
            self.connection.commit()


    class User:
        def __init__(self, connection):
            self.connection = connection

        def add_user(self,username,password,name,contact_information,user_id):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO book (username,password,name,contact_information) VALUES (?, ?, ?, ?)',
                        (username,password,name,contact_information))
            self.connection.commit()

        def edit_user(self,new_username,new_password,new_name,new_contact_information,user_id):
            cursor = self.connection.cursor()
            if new_password:
                cursor.execute('UPDATE user SET password = ? WHERE user_id = ?',
                        (new_password,user_id))
            elif new_name:
                cursor.execute('UPDATE user SET name = ? WHERE user_id = ?',
                        (new_name,user_id))
            elif new_contact_information:
                cursor.execute('UPDATE user SET contact_information = ? WHERE user_id = ?',
                        (new_contact_information,user_id))
            elif new_username:
                cursor.execute('UPDATE user SET username = ? WHERE user_id = ?',
                        (new_username,user_id))
            self.connection.commit()
            

        def delete_user(self,user_id):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM user WHERE user_id = ?',
                        (user_id,))
            self.connection.commit()

    class Transaction:
        def __init__(self, connection):
            self.connection = connection

        def check_out_book(self,user_id,book_id,due_date,status):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO transaction (user_id,book_id,due_date,status) VALUES (?, ?, ?, ?)',
                        (user_id,book_id,due_date,status))
            self.connection.commit()

        def check_in_book(self,new_status,transaction_id):
            cursor = self.connection.cursor()
            cursor.execute('UPDATE transaction SET status = ? WHERE transaction_id = ?',
                        (new_status,transaction_id))
            
            self.connection.commit()
            

        def view_transaction_history(self,transaction_id):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM transaction WHERE transaction_id = ?',
                        (transaction_id,))
            self.connection.commit()
        def view_transaction_history(self,transaction_id):
          cursor = self.connection.cursor()
          cursor.execute('DELETE FROM transaction WHERE transaction_id = ?',
                       (transaction_id,))
<<<<<<< HEAD
        self.connection.commit()
    #Lists and Tuples
        
        My_list = [Book, User, Librarian, Publisher]
        My_tuple = (Transaction )

    #Dictionaries - Collections Module
        
        book_details = {"ISBN": "book_details"}
        BookRecord = namedtuple ("BookRecord", ["title","author","genre","ISBN","quantity","publication_year"])  
        book_details["0102030405"] = BookRecord("Junior Level Books              Introduction to Computer","Amit Garg","IT","978-93-5019-561-1",4,2011) 
        book_details["1121315121"] = BookRecord(" Client Server Computing","Lalit Kumar","IT","978-93-8067-432-2",1,2012) 
        book_details["21315121314"] = BookRecord(" Data Structure Using C","Sharad Kumar Verma","IT","978-93-5163-389-1",2,2015) 
=======
          self.connection.commit()
          #Lists and Tuples
          My_list = [Book, User, Librarian, Publisher,  Transaction]
          My_tuple = (Transaction )
          #Dictionaries - Collections Module
           book_details = {"ISBN": "book_details"}
          BookRecord = namedtuple ("BookRecord", ["title","author","genre","ISBN","quantity","publication_year"])  
          book_details["0102030405"] = BookRecord("Junior Level Books              Introduction to Computer","Amit Garg","IT","978-93-5019-561-1",4,2011) 
          book_details["1121315121"] = BookRecord(" Client Server Computing","Lalit Kumar","IT","978-93-8067-432-2",1,2012) 
          book_details["21315121314"] = BookRecord(" Data Structure Using C","Sharad Kumar Verma","IT","978-93-5163-389-1",2,2015) 
>>>>>>> fc5670076313459a53d99801377570d417e0afbc

          ISBN = "0102030405"
          print("Book details for ISBN", ISBN, book_details.get(ISBN))

          Book_by_genre = defaultdict(list)
          for ISBN, details in book_details.items():
              genre = details.genre
              Book_by_genre[genre].append(ISBN)

<<<<<<< HEAD
    #OOP Concepts:
=======
          print("Books grouped by genre:")
          for genre, ISBN_list in Book_by_genre.items():
              print(genre + ":")
          for ISBN in ISBN_list:
              print(" *", book_details[ISBN].title)
>>>>>>> fc5670076313459a53d99801377570d417e0afbc

