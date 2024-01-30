import sqlite3
from collections import namedtuple, defaultdict


class LibraryManagementSystem:
    librarians_list = []
    publishers_list = []
    books_list = []
    users_list = []
    transactions_list = []
    ISBN_tuple = ()

    def __init__(self):
        self.connection = sqlite3.connect('librarysystem.db')
        self.cursor = self.connection.cursor()
        self.create_tables()        
    
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
            username text primary key,
            password text,
            name text,
            contact_information text
            )  
            ''')
        cursor.execute('''
            create table if not exists transaction(
            transaction_id primary key autoincrement,
            username integer,
            ISBN integer,
            due_date date,
            status text,
            foreign key (username) references user (username),
            foreign key (ISBN) references book (ISBN),
            )  
            ''')
        connection.commit()
        cursor.close()


    class Administrator:
        def __init__(self, connection):
            self.connection = connection

        def add_librarian(self, username, password, name, contact_information):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO librarian (username, password, name, contact_information) VALUES (?, ?, ?, ?)',
                           (username, password, name, contact_information))
            LibraryManagementSystem.librarians_list.append(username, password, name, contact_information)
            self.connection.commit()

        def edit_librarian(self, username, new_password, new_name, new_contact_information):
            cursor = self.connection.cursor()

            if new_password:
                cursor.execute('UPDATE librarian SET password = ? WHERE username = ?',
                               (new_password, username))

                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == username:
                        librarian_data = (
                            librarian_data[0], new_password, librarian_data[2], librarian_data[3])

            elif new_contact_information:
                cursor.execute('UPDATE librarian SET contact_information = ? WHERE username = ?',
                               (new_contact_information, username))

                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == username:
                        librarian_data = (
                            librarian_data[0], librarian_data[1], librarian_data[2], new_contact_information)

            elif new_name:
                cursor.execute('UPDATE librarian SET username = ? WHERE username = ?',
                               (new_name, username))

                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == username:
                        librarian_data = (
                            librarian_data[0], librarian_data[1], new_name, librarian_data[3])

            self.connection.commit()

        def delete_librarian(self, username):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM librarian WHERE username = ?',
                           (username,))

            LibraryManagementSystem.librarians_list = [
                data for data in LibraryManagementSystem.librarians_list if data[0] != username]

            self.connection.commit()

        def add_publisher(self, publisher_name, address, contact_details):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO publisher (publisher_name, address, contact_details) VALUES (?, ?, ?)',
                           (publisher_name, address, contact_details))

            LibraryManagementSystem.publishers_list.append(
                (publisher_name, address, contact_details))

            self.connection.commit()

        def edit_publisher(self, publisher_name, new_address, new_contact_details):
            cursor = self.connection.cursor()
            if new_address:
                cursor.execute('UPDATE publisher SET address = ? WHERE publisher_name = ?',
                               (new_address, publisher_name))

                for publisher_data in LibraryManagementSystem.publishers_list:
                    if publisher_data[0] == publisher_name:
                        publisher_data = (
                            publisher_data[0], new_address, publisher_data[2])

            elif new_contact_details:
                cursor.execute('UPDATE publisher SET contact_details = ? WHERE publisher_name = ?',
                               (new_contact_details, publisher_name))

                for publisher_data in LibraryManagementSystem.publishers_list:
                    if publisher_data[0] == publisher_name:
                        publisher_data = (
                            publisher_data[0], publisher_data[1], new_contact_details)

            self.connection.commit()

        def delete_publisher(self, publisher_name):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM publisher WHERE publisher_name = ?',
                           (publisher_name,))

            LibraryManagementSystem.publishers_list = [
                data for data in LibraryManagementSystem.publishers_list if data[0] != publisher_name]

            self.connection.commit()

        def add_user(self, username, password, name, contact_information):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO user (username, password, name, contact_information) VALUES (?, ?, ?, ?)',
                           (username, password, name, contact_information))
            LibraryManagementSystem.users_list.append()

            #
            #
            #
        




    class Librarian:
        def __init__(self,connection, username, password, name, contact_information):
            self.connection = connection
            self.username = username
            self.password = password
            self.name = name
            self.contact_information = contact_information

        def add_librarian(self,username,password,name,contact_information):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO librarian (username, password, name, contact_information) VALUES (?, ?, ?, ?)',
                        (username, password, name, contact_information))
            LibraryManagementSystem.librarians_list.append(self.username, self.password, self.name, self.contact_information)
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
                    if librarian_data[0] == username:
                        librarian_data = (librarian_data[0], librarian_data[1], librarian_data[2], new_contact_information)

            elif new_name:
                cursor.execute('UPDATE librarian SET username = ? WHERE username = ?',
                        (new_name,username))
                
                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == username:
                        librarian_data = (librarian_data[0], librarian_data[1], new_name, librarian_data[3])
            
            self.connection.commit()

        def delete_librarian(self,username):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM librarian WHERE username = ?',
                        (username,))
            
            LibraryManagementSystem.librarians_list = [data for data in LibraryManagementSystem.librarians_list if data[0] != username]


            self.connection.commit()

        def display_info(self):
            print(f"Librarian {self.name}, username {self.username}, password {self.password}, contact information {self.contact_information}")


    class Publisher:
        def __init__(self, connection,publisher_name,address,contact_details):
            self.connection = connection
            self.publisher_name = publisher_name
            self.address = address
            self.contact_details = contact_details

        def add_publisher(self,publisher_name,address,contact_details):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO publisher (publisher_name,address,contact_details) VALUES (?, ?, ?)',
                        (publisher_name,address,contact_details))
            
            LibraryManagementSystem.publishers_list.append(self.publisher_name, self.address, self.contact_details)

            self.connection.commit()
            
        def edit_publisher(self,publisher_name,new_address,new_contact_details):
            cursor = self.connection.cursor()
            if new_address:
                cursor.execute('UPDATE publisher SET address = ? WHERE publisher_name = ?',
                        (new_address,publisher_name))
                
                for publisher_data in LibraryManagementSystem.publishers_list:
                    if publisher_data[0] == publisher_name:
                        publisher_data = (publisher_data[0], new_address, publisher_data[2])

            elif new_contact_details:
                cursor.execute('UPDATE publisher SET contact_details = ? WHERE publisher_name = ?',
                        (new_contact_details,publisher_name))
                
                for publisher_data in LibraryManagementSystem.publishers_list:
                    if publisher_data[0] == publisher_name:
                        publisher_data = (publisher_data[0], publisher_data[1], new_contact_details)
            
            self.connection.commit()

        def delete_publisher(self,publisher_name):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM publisher WHERE publisher_name = ?',
                        (publisher_name,))
            
            LibraryManagementSystem.publishers_list = [data for data in LibraryManagementSystem.publishers_list if data[0] != publisher_name]

            self.connection.commit()

        def display_info(self):
            print(f"Publisher {self.publisher_name}, address {self.address}, contact details {self.contact_details}")

    class Book:
        def __init__(self, connection):
            self.connection = connection

        def add_book(self,title,author,genre,ISBN,quantity,publication_year):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO book (title,author,genre,ISBN,quantity,publication_year) VALUES (?, ?, ?, ?, ?, ?)',
                        (title,author,genre,ISBN,quantity,publication_year))
            self.connection.commit()
            
        def edit_book(self,new_title,new_author,new_genre,ISBN,new_quantity,new_publication_year):
            cursor = self.connection.cursor()
            if new_title:
                cursor.execute('UPDATE book SET title = ? WHERE ISBN = ?',
                        (new_title,ISBN))
            elif new_author:
                cursor.execute('UPDATE book SET author = ? WHERE ISBN = ?',
                        (new_author,ISBN))
            elif new_genre:
                cursor.execute('UPDATE book SET genre = ? WHERE ISBN = ?',
                        (new_genre,ISBN))
            elif new_quantity:
                cursor.execute('UPDATE book SET quantity = ? WHERE ISBN = ?',
                        (new_quantity,ISBN))
            elif new_publication_year:
                cursor.execute('UPDATE book SET publication_year = ? WHERE ISBN = ?',
                        (new_publication_year,ISBN))  
            self.connection.commit()
            

        def delete_book(self,ISBN):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM book WHERE ISBN = ?',
                        (ISBN,))
            self.connection.commit()

        def display_info(self):
            print(f"Book title {self.tile}, author {self.author}, genre {self.genre}, ISBN {self.ISBN}, quantity {self.quantity}, publication year {self.publication_year}")

    class User:
        def __init__(self, connection):
            self.connection = connection

        def add_user(self,username,password,name,contact_information):
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO user (username,password,name,contact_information) VALUES (?, ?, ?, ?)',
                        (username,password,name,contact_information))
            self.connection.commit()

        def edit_user(self,username,new_password,new_name,new_contact_information):
            cursor = self.connection.cursor()
            if new_password:
                cursor.execute('UPDATE user SET password = ? WHERE username = ?',
                        (new_password,username))
            elif new_name:
                cursor.execute('UPDATE user SET name = ? WHERE username = ?',
                        (new_name,username))
            elif new_contact_information:
                cursor.execute('UPDATE user SET contact_information = ? WHERE username = ?',
                        (new_contact_information,username))
                
            self.connection.commit()
            

        def delete_user(self,username):
            cursor = self.connection.cursor()
            cursor.execute('DELETE FROM user WHERE username = ?',
                        (username,))
            self.connection.commit()

        def display_info(self):
            print(f"Username {self.username}, password {self.password}, name {self.name}, contact information {self.contact_information}")


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
            cursor.execute('SELECT * transaction WHERE transaction_id = ?',
                        (transaction_id,))
            self.connection.commit()
#          #Lists and Tuples
        
#         My_list = [Book, User, Librarian, Publisher]
#         My_tuple = (Transaction )

#     #Dictionaries - Collections Module
        
#         book_details = {"ISBN": "book_details"}
#         BookRecord = namedtuple ("BookRecord", ["title","author","genre","ISBN","quantity","publication_year"])  
#         book_details["0102030405"] = BookRecord("Junior Level Books              Introduction to Computer","Amit Garg","IT","978-93-5019-561-1",4,2011) 
#         book_details["1121315121"] = BookRecord(" Client Server Computing","Lalit Kumar","IT","978-93-8067-432-2",1,2012) 
#         book_details["21315121314"] = BookRecord(" Data Structure Using C","Sharad Kumar Verma","IT","978-93-5163-389-1",2,2015) 
            
    
#           ISBN = "0102030405"
#           print("Book details for ISBN", ISBN, book_details.get(ISBN))

#           Book_by_genre = defaultdict(list)
#           for ISBN, details in book_details.items():
#               genre = details.genre
#               Book_by_genre[genre].append(ISBN)
#             OOP Concepts:

#           print("Books grouped by genre:")
#           for genre, ISBN_list in Book_by_genre.items():
#               print(genre + ":")
#           for ISBN in ISBN_list:
#               print(" *", book_details[ISBN].title)

