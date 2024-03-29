import sqlite3
from collections import namedtuple, defaultdict


class LibraryManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect('librarysystem1.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

        self.librarians_list = []
        self.publishers_list = []
        self.books_list = []
        self.users_list = []
        self.transactions_list = []
        self.ISBN_tuple = ()
        self.books_dict = {}
    
    def create_tables(self):
        self.cursor.execute('''
            create table if not exists librarian(
            username text primary key,
            password text,
            name text,
            contact_information text
            )  
            ''')
        self.cursor.execute('''
            create table if not exists publisher(
            publisher_name text primary key,
            address text,
            contact_details text
            )  
            ''')
        self.cursor.execute('''
            create table if not exists book(
            title text,
            author text,
            genre text,
            ISBN integer primary key,
            quantity integer,
            publication_year integer
            )  
            ''')
        self.cursor.execute('''
            create table if not exists user(
            username text primary key,
            password text,
            name text,
            contact_information text
            )  
            ''')
        self.cursor.execute('''
            create table if not exists transaction1(
            transaction_id integer primary key autoincrement,
            username text,
            ISBN integer,
            due_date date,
            status text,
            foreign key (username) references user (username),
            foreign key (ISBN) references book (ISBN)
            )
            ''')
        self.conn.commit()

    class Librarian:
        def __init__(self, username, password, name, contact_information):
            self.username = username
            self.password = password
            self.name = name
            self.contact_information = contact_information

        def add_librarian(self,username,password,name,contact_information):
            self.cursor.execute('INSERT INTO librarian (username, password, name, contact_information) VALUES (?, ?, ?, ?)',
                        (username, password, name, contact_information))
            LibraryManagementSystem.librarians_list.append(self.username, self.password, self.name, self.contact_information)
            self.conn.commit()
            
        def edit_librarian(self,username,new_password,new_name,new_contact_information):

            if new_password:
                self.cursor.execute('UPDATE librarian SET password = ? WHERE username = ?',
                        (new_password,username))
                
                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == new_password:
                        librarian_data = (librarian_data[0], new_password, librarian_data[2], librarian_data[3])

            elif new_contact_information:
                self.cursor.execute('UPDATE librarian SET contact_information = ? WHERE username = ?',
                        (new_contact_information,username))
                
                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == username:
                        librarian_data = (librarian_data[0], librarian_data[1], librarian_data[2], new_contact_information)

            elif new_name:
                self.cursor.execute('UPDATE librarian SET username = ? WHERE username = ?',
                        (new_name,username))
                
                for librarian_data in LibraryManagementSystem.librarians_list:
                    if librarian_data[0] == username:
                        librarian_data = (librarian_data[0], librarian_data[1], new_name, librarian_data[3])
            
            self.conn.commit()

        def delete_librarian(self,username):
            self.cursor.execute('DELETE FROM librarian WHERE username = ?',
                        (username,))       
            LibraryManagementSystem.librarians_list = [data for data in LibraryManagementSystem.librarians_list if data[0] != username]
            self.conn.commit()

        def display_info(self):
            print(f"Librarian {self.name}, username {self.username}, password {self.password}, contact information {self.contact_information}")


    class Publisher:
        def __init__(self,publisher_name,address,contact_details):
            self.publisher_name = publisher_name
            self.address = address
            self.contact_details = contact_details

        def add_publisher(self,publisher_name,address,contact_details):
            self.cursor.execute('INSERT INTO publisher (publisher_name,address,contact_details) VALUES (?, ?, ?)',
                        (publisher_name,address,contact_details))
            
            LibraryManagementSystem.publishers_list.append(self.publisher_name, self.address, self.contact_details)

            self.conn.commit()
            
        def edit_publisher(self,publisher_name,new_address,new_contact_details):
            if new_address:
                self.cursor.execute('UPDATE publisher SET address = ? WHERE publisher_name = ?',
                        (new_address,publisher_name))
                
                for publisher_data in LibraryManagementSystem.publishers_list:
                    if publisher_data[0] == publisher_name:
                        publisher_data = (publisher_data[0], new_address, publisher_data[2])

            elif new_contact_details:
                self.cursor.execute('UPDATE publisher SET contact_details = ? WHERE publisher_name = ?',
                        (new_contact_details,publisher_name))
                
                for publisher_data in LibraryManagementSystem.publishers_list:
                    if publisher_data[0] == publisher_name:
                        publisher_data = (publisher_data[0], publisher_data[1], new_contact_details)
            
            self.conn.commit()

        def delete_publisher(self,publisher_name):
            self.cursor.execute('DELETE FROM publisher WHERE publisher_name = ?',
                        (publisher_name,))
            
            LibraryManagementSystem.publishers_list = [data for data in LibraryManagementSystem.publishers_list if data[0] != publisher_name]

            self.conn.commit()

        def display_info(self):
            print(f"Publisher {self.publisher_name}, address {self.address}, contact details {self.contact_details}")

    class Book:
        def __init__(self, title,author,genre,ISBN,quantity,publication_year):
            self.title = title
            self.author = author
            self.genre = genre
            self.ISBN = ISBN
            self.quantity = quantity
            self.publication_year = publication_year            

        def add_book(self,title,author,genre,ISBN,quantity,publication_year):
            self.cursor.execute('INSERT INTO book (title,author,genre,ISBN,quantity,publication_year) VALUES (?, ?, ?, ?, ?, ?)',
                        (title,author,genre,ISBN,quantity,publication_year))

            LibraryManagementSystem.books_list.append(self.title, self.author,self.genre,self.ISBN, self.quantity,self.publication_year)

            book_details = {
                'title': title,
                'author': author,
                'genre': genre,
                'ISBN': ISBN,
                'quantity': quantity,
                'publication_year': publication_year
            }
            LibraryManagementSystem.books_dict[ISBN] = book_details

            LibraryManagementSystem.ISBN_tuple += (ISBN,)

            self.conn.commit()    

            
        def edit_book(self,new_title,new_author,new_genre,ISBN,new_quantity,new_publication_year):
            if new_title:
                self.cursor.execute('UPDATE book SET title = ? WHERE ISBN = ?',
                        (new_title,ISBN))                
                for books_data in LibraryManagementSystem.books_list:
                        if books_data[0] == new_title:
                            books_data = (new_title, books_data[1], books_data[2],books_data[3],books_data[4],books_data[5],books_data[6],books_data[7])
                LibraryManagementSystem.books_dict[ISBN]['title'] = new_title

            elif new_author:
                self.cursor.execute('UPDATE book SET author = ? WHERE ISBN = ?',
                        (new_author,ISBN))
                for books_data in LibraryManagementSystem.books_list:
                        if books_data[0] == new_author:
                            books_data = ( books_data[0],new_author, books_data[2],books_data[3],books_data[4],books_data[5],books_data[6],books_data[7])
                LibraryManagementSystem.books_dict[ISBN]['author'] = new_author

            elif new_genre:
                self.cursor.execute('UPDATE book SET genre = ? WHERE ISBN = ?',
                        (new_genre,ISBN))
                for books_data in LibraryManagementSystem.books_list:
                        if books_data[0] == new_genre:
                            books_data = ( books_data[0], books_data[1], new_genre, books_data[3],books_data[4],books_data[5],books_data[6], books_data[7])
                LibraryManagementSystem.books_dict[ISBN]['genre'] = new_genre

            elif new_quantity:
                self.cursor.execute('UPDATE book SET quantity = ? WHERE ISBN = ?',
                        (new_quantity,ISBN))
                for books_data in LibraryManagementSystem.books_list:
                        if books_data[0] == new_quantity:
                            books_data = ( books_data[0], books_data[1],books_data[2], books_data[3],new_quantity, books_data[4],books_data [5],books_data[6], books_data[7])
                LibraryManagementSystem.books_dict[ISBN]['quantity'] = new_quantity


            elif new_publication_year:
                self.cursor.execute('UPDATE book SET publication_year = ? WHERE ISBN = ?',
                        (new_publication_year,ISBN))
                for books_data in LibraryManagementSystem.books_list:
                        if books_data[0] == new_publication_year:
                            books_data = ( books_data[0], books_data[1],books_data[2], books_data[3],books_data[4],new_publication_year, [6],books_data[7])
                LibraryManagementSystem.books_dict[ISBN]['publication_year'] = new_publication_year

            self.conn.commit()
            

        def delete_book(self,ISBN):
            self.cursor.execute('DELETE FROM book WHERE ISBN = ?',
                        (ISBN,))
            
            LibraryManagementSystem.books_list = [data for data in LibraryManagementSystem.books_list if data[0] != ISBN]

            if ISBN in LibraryManagementSystem.books_dict:
                del LibraryManagementSystem.books_dict[ISBN]
            self.conn.commit()

        def display_info(self):
            print(f"Book title {self.title}, author {self.author}, genre {self.genre}, ISBN {self.ISBN}, quantity {self.quantity}, publication year {self.publication_year}")

        def search_books_by_title(self, search_title):
            matching_books = []
            for ISBN, book_details in LibraryManagementSystem.books_dict.items():
                if search_title.lower() in book_details['title'].lower():
                    matching_books.append(book_details)
            return matching_books

        def search_books_by_author(self, author):
            matching_books = []
            for ISBN, book_details in LibraryManagementSystem.books_dict.items():
                if author.lower() in book_details['author'].lower():
                    matching_books.append(book_details)
            return matching_books
        
                    
        def filter_books_by_genre(self, genre):
            self.cursor.execute('SELECT * FROM book WHERE genre = ?', (genre,))
            books_data = self.cursor.fetchall()
            if books_data:
                filtered_books = []
                for book_data in books_data:
                    book_details = {
                        'title': book_data[0],
                        'author': book_data[1],
                        'genre': book_data[2],
                        'ISBN': book_data[3],
                        'quantity': book_data[4],
                        'publication_year': book_data[5]
                    }
                    filtered_books.append(book_details)
                return filtered_books
            else:
                return None
            
        def filter_books_by_year_range(self, start_year, end_year):
            filtered_books = [book_details for book_details in LibraryManagementSystem.books_dict.values()
                              if start_year <= book_details['publication_year'] <= end_year]
            return filtered_books
        
        

    class User:
        def __init__(self, username,password,name,contact_information):
            self.username = username
            self.password = password
            self.name = name
            self.contact_information = contact_information

        def add_user(self,username,password,name,contact_information):
            self.cursor.execute('INSERT INTO user (username,password,name,contact_information) VALUES (?, ?, ?, ?)',
                        (username,password,name,contact_information))
            LibraryManagementSystem.users_list.append(self.username,self.password,self.name,self.contact_information)
            
            self.conn.commit()


        def edit_user(self,username,new_password,new_name,new_contact_information):
            
            if new_password:
                self.cursor.execute('UPDATE user SET password = ? WHERE username = ?',
                        (new_password,username))
                for users_data in LibraryManagementSystem.users_list:
                        if users_data[0] == new_password:
                            users_data = (users_data[0], new_password, users_data[1],users_data[2],users_data, [3],users_data[4])

            elif new_name:
                self.cursor.execute('UPDATE user SET name = ? WHERE username = ?',
                        (new_name,username))
                for users_data in LibraryManagementSystem.users_list:
                        if users_data[0] == new_name:
                            users_data = (users_data[0],users_data[1], users_data[2],new_name,users_data, [3],users_data[4])
                
            elif new_contact_information:
                self.cursor.execute('UPDATE user SET contact_information = ? WHERE username = ?',
                        (new_contact_information,username))
                for users_data in LibraryManagementSystem.users_list:
                        if users_data[0] == new_contact_information:
                            users_data = (users_data[0],users_data[1], users_data[2],users_data, [3],new_contact_information, users_data[4])
                
            self.conn.commit()
            

        def delete_user(self,username):
            self.cursor.execute('DELETE FROM user WHERE username = ?',
                        (username,))
            
            self.conn.commit()

        def display_info(self):
            print(f"Username {self.username}, password {self.password}, name {self.name}, contact information {self.contact_information}")

        def search_user(self, username):
            self.cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
            user_data = self.cursor.fetchall()
            if user_data:
                user_details = {
                    'username': user_data[0],
                    'password': user_data[1],
                    'name': user_data[2],
                    'contact_information': user_data[3]
                }
                return user_details
            else:
                return None
            
        def filter_users_by_name(self, name):
            filtered_users = [user for user in LibraryManagementSystem.users_list if name.lower() in user['name'].lower()]
            return filtered_users
        
        def filter_users_by_registration_year_range(self, start_year, end_year):
            filtered_users = [user_details for user_details in LibraryManagementSystem.users_dict.values()
                              if start_year <= user_details['registration_year'] <= end_year]
            return filtered_users


    class Transaction:
        def __init__(self):
            pass

        # def check_out_book(self,user_id,book_id,due_date,status):
        #     cursor = self.connection.cursor()
        #     cursor.execute('INSERT INTO transaction (user_id,book_id,due_date,status) VALUES (?, ?, ?, ?)',
        #                 (user_id,book_id,due_date,status))            
        #     LibraryManagementSystem.transactions_list.append(self.user_id,self.book_id,self.due_date,self.status)                        
        #     self.connection.commit()

        # def check_in_book(self,new_status,transaction_id):
        #     cursor = self.connection.cursor()
        #     cursor.execute('UPDATE transaction SET status = ? WHERE transaction_id = ?',
        #                 (new_status,transaction_id))
        #     for transactions_data in LibraryManagementSystem.transactions_list:
        #         if Users_data[0] == new_check_in_book:
        #             Users_data = (Users_data[0],Users_data[1], Users_data[2],Users_data, [3],new_contact_information, Users_data[4])                       
        #     self.connection.commit()
            
        # def view_transaction_history(self,transaction_id):
        #     cursor = self.connection.cursor()
        #     cursor.execute('SELECT * transaction WHERE transaction_id = ?',
        #                     (transaction_id,))  
        #     self.connection.commit()

        def check_out_book(self, user, book, due_date, status):
            self.cursor.execute('INSERT INTO transaction (user_id, book_id, due_date, status) VALUES (?, ?, ?, ?)',
                        (user.id, book.id, due_date, status))
            self.conn.commit()

            transaction_details = {
                'user': user,
                'book': book,
                'due_date': due_date,
                'status': status
            }
            LibraryManagementSystem.transactions_list.append(transaction_details)

        def check_in_book(self, new_status, transaction_id):
            self.cursor.execute('UPDATE transaction SET status = ? WHERE transaction_id = ?',
                        (new_status, transaction_id))
            self.conn.commit()

            for transaction_details in LibraryManagementSystem.transactions_list:
                if transaction_details['id'] == transaction_id:
                    transaction_details['status'] = new_status

        def view_transaction_history(self, user_id):
            self.cursor.execute('SELECT * FROM transaction WHERE user_id = ?', (user_id,))
            transactions_data = self.cursor.fetchall()
            self.conn.commit()

            transaction_history = []
            for transaction_data in transactions_data:
                transaction_details = {
                    'user': transaction_data[1],
                    'book': transaction_data[2],
                    'due_date': transaction_data[3],
                    'status': transaction_data[4]
                }
                transaction_history.append(transaction_details)

            return transaction_history



#         Dictionaries - Collections Module
        
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

def main():

    library = LibraryManagementSystem()

    while True:
        print("\n==== Menu ====")
        print("1. Administrator")
        print("2. Librarian")
        print("3. User")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("----Admin section----")
            print("1. Librarian management")
            print("2. User management")
            print("3. Publisher management")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                print("----Librarian management----")
                print("1. Add a Librarian")
                print("2. Edit a Librarian")
                print("3. Delete a Librarian")
                print("4. Exit")
                choice = input("Enter your choice (1-4): ")
                
                if choice == '1':
                    print("----Add a librarian----")
                    username = input("Please give me the username: ")
                    password = input("Please give me the password: ")
                    name = input("Please give the name: ")
                    contact_information = input("Please give the contact information: ")

                    library.Librarian.add_librarian(username, password, name, contact_information)
                    
                elif choice == '2':
                    print("----Edit a librarian----")
                    username = input("Please give me the username: ")
                    password = input("Please give me the new password: ")
                    name = input("Please give the new name: ")
                    contact_information = input("Please give the new contact information: ")

                    library.Librarian.edit_librarian(username,password,name,contact_information)

                elif choice == '3':
                    print("----Delete a librarian----")
                    username = input("Please give the username of the librarian ")

                    LibraryManagementSystem.delete_librarian(username)

                elif choice == '4':
                    print("----Exit----")
                    break

            if choice == '2':
                print("----User management----")
                print("1. Add a User")
                print("2. Edit a User")
                print("3. Delete a User")
                print("4. Exit")
                choice = input("Enter your choice (1-4): ")
                if choice == '1':
                    print("----Add a user----")
                    username = input("Please give me your username: ")
                    password = input("Please give me the new password: ")
                    name = input("Please give the new name: ")
                    contact_information = input("Please give the new contact information: ")

                    LibraryManagementSystem.add_user(username,password,name,contact_information)

                if choice == '2':
                    print("----Edit a user----")
                    username = input("Please give me the username: ")
                    password = input("Please give me the new password: ")
                    name = input("Please give the new name: ")
                    contact_information = input("Please give the new contact information: ")

                    LibraryManagementSystem.edit_user(username,password,name,contact_information)


    

if __name__ == "__main__":
    main()