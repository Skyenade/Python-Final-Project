

import sqlite3  ## to write the SQL queries
import datetime


## function to connect python to a database
def connect():
    return sqlite3.connect('Library.db')


class projectPython:
    def __init__(self):
        pass


class CommonUser(projectPython):
    def __init__(self, username, password, name, contactInfo):
        self.username = username
        self.password = password
        self.name = name
        self.contactInfo = contactInfo


## Librarian class with same as Common User attributes
class Librarian(CommonUser):
    def __init__(self):
        super.__init__()  ## super to access the attributes from Common User class {Inheritance}


## User class with same as Common User attributes    
class User(CommonUser):
    def __init__(self):
        super.__init__()  ## super to access the attributes from Common User class {Inheritance}


## Publisher class with its attributes
class Publisher(projectPython):
    def __init__(self, publishername, address, contactdetails):
        self.publishername = publishername
        self.address = address
        self.contactdetails = contactdetails


## Book class with attributes        
class Book(projectPython):
    def __init__(self, title, author, genre, ISBN, quantity, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.ISBN = ISBN
        self.quantity = quantity
        self.publication_year = publication_year


## Transaction Class with attributes           
class Transaction(projectPython):
    def __init__(self, username, ISBN, duedate, duestatus):
        self.username = username
        self.ISBN = ISBN
        self.duedate = duedate
        self.duestatus = duestatus




## User management with storage - add_record , modify_record, delete_record

class CommonUserManagement(CommonUser):
    def __init__(self):
        self.storage = []

    ## method to add an entry  for both librarian and user entries
    def add_entry(self, username, password, name, contactInfo):
        self.storage.append(
            {"Username is ": username, "password ": password, "name ": name, "contactInfo is": contactInfo})

    ## method to delete an entry  for both librarian and user entries
    def delete_entry(self, username):
        for entry in self.storage:
            if entry["Username is "] == username:
                self.storage.remove(entry)

    ## method to update an entry based on primary key value    for both librarian and user entries          
    def update_entry(self,username,new_password,new_name,new_contactInfo):
        for entry in self.storage:
            if entry["Username is "] == username:
                entry["password "] = new_name
                entry["name "] = new_password
                entry["contactInfo is"] = new_contactInfo
                break
                



## Publisher management class to add, modify and delete entries

class PublisherManagement(Publisher):
    def __init__(self):
        self.publishstorage = []

    ## method to add entry    
    def add_entry(self, publishername, address, contactdetails):
        self.publishstorage.append(
            {"Publisher name is ": publishername, "address ": address, "contactdetails are": contactdetails})

    ## method to delete entry
    def delete_entry(self, publishername):
        for entry in self.publishstorage:
            if entry["publisher name is "] == publishername:
                self.publishstorage.remove(entry)

    ##method to update entry
    def update_entry(self,publishername,new_address,new_contactdetails):
        for entry in self.publishstorage:
            if entry["Publisher name is "] == publishername:
                entry["address "] = new_address
                entry["contactdetails are"] = new_contactdetails
                break



## Book management class to add, modify and delete entries

class BookManagement(Book):
    def __init__(self):
        self.bookstorage = []

    ## method to add a book entry    
    def add_book(self, title, author, genre,ISBN,quantity,publication_year):
            self.bookstorage.append(
                {"title ": title, "author ": author, "genre ": genre, "ISBN ": ISBN, "quantity ": quantity, "publication year " : publication_year})

    ## method to delete entry
    def delete_book(self, ISBN):
        for entry in self.bookstorage:
            if entry["ISBN "] == ISBN:
                self.bookstorage.remove(entry)

    ## method to update entry  
    def update_book(self,new_title, new_author, new_genre,ISBN,new_quantity,new_publication_year):
        for entry in self.bookstorage:
            if entry["ISBN "] == ISBN:
                entry["title "] = new_title
                entry["author "] = new_author
                entry["genre "] = new_genre
                entry["quantity "] = new_quantity
                entry["publication year "] = new_publication_year
                break


class TransactionManagement(Transaction):

    def __init__(self):
        self.Trans_storage = []

    ##checkout books records
    def check_out_book(self, CommonUser, ISBN, duedate, duestatus):
        transactionrecord = (
            {"User :": CommonUser, "Book ISBN": ISBN, "Due date is: ": duedate, "status : ": duestatus})
        self.Trans_storage.append(transactionrecord)



    ##check in recods with status value updated        
    def check_in_book(self, CommonUser, ISBN):
        for transactionrecord in self.Trans_storage:
            if transactionrecord["User :"] == CommonUser and transactionrecord["Book ISBN"] == ISBN and transactionrecord["status :"] == "Checked Out":
                transactionrecord["status :"] = "Returned"
                print(f"Book with ISBN {ISBN} checked in successfully by {CommonUser}.")
                return
        print(f"No matching check-out record found for user {CommonUser} and book ISBN {ISBN}.")




    def transaction_history(self):
        if self.Trans_storage:
            print("Transaction History: ")
            for i, self.Trans_storage in enumerate(self.Trans_storage, start=1):
                print(f"Transaction {i}")
                for key, value in self.Trans_storage.items():
                    print(f"{key}: {value}")
        else:
            print("No transactions found")



## Database class to implement the tables and functions

class Database:
    def __init__(self, db_file='PythonProject.db'):  ##file storage and filename
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):  ## Librarian table with 4 columns
        self.cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS Librarian ( 
                username TEXT primary key not null, 
                password TEXT,
                name TEXT,
                contactInfo TEXT
        );      
    ''')

        ## Publisher table with 3 columns
        self.cursor.execute('''
                  CREATE TABLE if not exists Publisher(
                      publishername text primary key not null, 
                      address text,
                      contactdetails text
                  ) ;              
            
            ''')

        ## User table with 4 columns, with username as primary key
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS User (
                username TEXT primary key not null, 
                password TEXT,
                name TEXT,
                contactInfo TEXT
        );      
    ''')
        ## Books table with 6 columns, ISBN beign the primary key
        self.cursor.execute('''
                    create table if not exists Books(
                        title text,
                        author text,
                        genre text,
                        ISBN integer primary key not null,
                        quantity integer,
                        publication_year integer );
                        ''')

        ## Transactions table with 2 foreign keys from Users and Books tables
        self.cursor.execute('''
                    create table if not exists Transactions(
                      username text,
                      ISBN integer,
                      duedate date,
                      duestatus text not null,
                      foreign key (username) references  User (username),
                      foreign key (ISBN) references  Books(ISBN));
                ''')

        ## to commit the changes
        self.conn.commit()

        ## database method to insert the librarian records

  #  def insert_librarian(self, librarian):

    

  #  def delete_librarian(self, username):


    ## database method to update the librarian records      
   # def update_librarian(self, username, password, name, contactInfo):


        ## database method to insert the pubilsher records

   # def insert_publisher(self, publisher):

      

    #### database method to delete the publisher records          
   # def delete_publisher(self, publishername):
      

    ## database method to update the publisher records      
   # def update_publisher(self, publishername, address, contactdetails):
       

        ## database method to insert the User records

    #def insert_user(self, user):
      

    #### database method to delete the user records          
  
    ## database method to update the user records      
 

    #def insert_book(self, book):
   

    ## database method to delete the book records          


    ## database method to update the book records      
    #def update_book(self, ISBN, title, author, genre, quantity, publication_year):
  

        ## database method to insert the transaction records

    def check_out_book(self, transaction1):
        userCheck = self.cursor.execute('select username from User where (username = ?);',
                                        (transaction1.username,)).fetchone()
        ISBNcheck = self.cursor.execute('select ISBN from Books where (ISBN = ?);', (transaction1.ISBN,)).fetchone()
        if userCheck is not None:
            if ISBNcheck is not None:
                self.cursor.execute('''
                                    insert into Transactions (username, ISBN, duedate,duestatus )
                                    values (?,?,?,? );
                                    ''', (
                    transaction1.username, transaction1.ISBN, transaction1.duedate, transaction1.duestatus))
            else:
                print("No book is found in inventory")
        else:
            print("No user is found")

            ## database method to insert the checkin  records

   # def check_in_book(self, transaction2):
      

    def view_transaction_history(self, transaction4):
        print("user input: ", transaction4)
        transaction4 = '%' + transaction4 + '%'

        query = """
            SELECT * FROM Transactions 
            WHERE username LIKE ?
            """
        self.cursor.execute(query, (transaction4,))

        history = self.cursor.fetchall()

        if history:
            for record in history:
                print("Book title:", record[0])
                print("Author:", record[1])
                print("Genre:", record[2])
                print("ISBN:", record[3])
                print()
        else:
            print("No transaction history found.")

    ## database method to search the books from books records
   # def search_books(self, search_query):
      

    ## database method to filter the book records based on genre              
    #def filter_books_by_genre(self, genre):


    ## database method to filter the users based on name
    #def filter_users_by_name(self, name):
      

    ## database method to filter the books records based on time of publication range
   # def filter_books_by_year_range(self, start_year, end_year):
     

    ## database method to find  the checked out books based on username
    # def find_checked_out_books(self, username):
   
        ## sorting books method based on publication year

    def sort_books(self, sort_criteria):
        if sort_criteria == 'title':
            query = "SELECT * FROM Books ORDER BY title"
        elif sort_criteria == 'author':
            query = "SELECT * FROM Books ORDER BY author"
        elif sort_criteria == 'publication_year':
            query = "SELECT * FROM Books ORDER BY publication_year"
        else:
            return []
        self.cursor.execute(query)
        books = self.cursor.fetchall()
        return books


if __name__ == "__main__":
    connection = connect()
    trialTest = projectPython()
    db = Database()

    ##Printing the main menu
    while True:
        print("==== Welcome to Library Management System ====")
        print("Please choose the role")
        print(" 1.Administator Section")
        print(" 2.Librarian Section")
        print(" 3.User Section")
        print(" 4.Exit")

        ## Asking the user for input
        mainchoice = input("Enter your choice (1-4): ")

        if mainchoice == '1':

            while True:

                ##Printing the  menu
                print("====Administration Section=====")
                print("1. Librarian Management")
                print("2. Publisher Management")
                print("3. User Management")
                print("4. Return to main menu")

                ## Asking the user for input
                adminchoice = input("Please choose between (1-4)")

                if adminchoice == '1':

                    ##Printing the  menu
                    while True:
                        print("===========Librarian Management Section=========")
                        print("1. Add a librarian to the database")
                        print("2. Edit a librarian from the database")
                        print("3. Remove a librarian from the database")
                        print("4. Return to Administrator Menu")

                        ## Asking the user for input
                        libChoice = input("Please choose between (1 - 4)")

                        if libChoice == '1':
                            username = input("Please enter the librarian username: ")
                            password = input("Please enter the password: ")
                            name = input("Please enter the name: ")
                            contactInfo = input("please enter the contact information: ")
                            lib1 = CommonUser(username, password, name, contactInfo)
                            db.insert_librarian(lib1)
                            print(f"{lib1} added to the database.")

                        elif libChoice == '2':
                            updateUsername = input("Please enter the librarian username to update from the table: ")
                            updatedpassword = input("Please enter the updated password: ")
                            updatename = input("Please enter the update name: ")
                            updateContactinfo = input("Please enter the updated contact details: ")
                            db.update_librarian(updateUsername, updatedpassword, updatename, updateContactinfo)
                            print(f"{updateUsername} record is updated")

                        elif libChoice == '3':
                            deleteusername = input("Please enter the librarian username to remove from the table")
                            db.delete_librarian(deleteusername)

                            ## Prompting the user the returning to the main menu
                        elif libChoice == '4':
                            print("Returning to admin menu, Thank you.")
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")


                elif adminchoice == '2':

                    ##Printing the  menu
                    while True:
                        print("====Publisher Management Section=====")
                        print("1. Add a publisher record")
                        print("2. Remove a publisher record")
                        print("3. Update a publisher record")
                        print("4. Return to Administrator Menu")

                        ## Asking the user for input
                        pubChoice = input("Please choose between (1-4)")

                        if pubChoice == '1':
                            publishername = input("Please enter the publisher username: ")
                            address = input("Please enter the address")
                            contactdetails = input("please enter the contact details")
                            pub1 = Publisher(publishername, address, contactdetails)
                            db.insert_publisher(pub1)
                            print(f"{pub1} added to the database.")

                        elif pubChoice == '2':
                            updatePublishername = input("Please enter the publisher name to update from the table")
                            updateaddress = input("Please enter the update address : ")
                            updateContactdetails = input("Please enter the updated contact details")
                            db.update_publisher(updatePublishername, updateaddress, updateContactdetails)
                            print(f"{updatePublishername} record is updated")
                        elif pubChoice == '3':
                            deleteusername = input("Please enter the publisher name to remove from the table")
                            db.delete_publisher(deleteusername)

                            ## Prompting the user the returning to the main menu
                        elif pubChoice == '4':
                            print("returning to main menu, Thank you.")
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")

                elif adminchoice == '3':

                    ##Printing the  menu
                    while True:
                        print("====User Management Section=====")
                        print("1. Add a User record")
                        print("2. Remove a User record")
                        print("3. Update a User record")
                        print("4. Find User")
                        print("5. Return to Administrator Menu")

                        ## Asking the user for input
                        userChoice = input("Please choose between (1-5)")

                        if userChoice == '1':
                            username = input("Please enter the User username: ")
                            password = input("Please enter the password")
                            name = input("Please enter the name")
                            contactInfo = input("please enter the contact information")
                            user1 = CommonUser(username, password, name, contactInfo)
                            db.insert_user(user1)
                            print(f"{user1} added to the storage.")

                        elif userChoice == '2':
                            updateUsername = input("Please enter the User username to update from the table")
                            updatedpassword = input("Please enter the updated password")
                            updatename = input("Please enter the update name: ")
                            updateContactinfo = input("Please enter the updated contact details")
                            db.update_user(updateUsername, updatedpassword, updatename, updateContactinfo)
                            print(f"{updateUsername} record is updated")

                        elif userChoice == '3':
                            deleteusername = input("Please enter the User username to remove from the table")
                            db.delete_user(deleteusername)

                        elif userChoice == '4':
                            findname = input("Please enter the name of the user to find")
                            db.filter_users_by_name(findname)

                            ## Prompting the user the returning to the main menu
                        elif userChoice == '5':
                            print("returning to Admin menu, Thank you.")
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")

                            ## Prompting the user the returning to the main menu
                elif adminchoice == '4':
                    print("Returning to the main menu, Thank you.!!")
                    break

                else:
                    print("Invalid input entered, please choose between (1-4)")

        elif mainchoice == '2':

            ##Printing the  menu
            while True:
                print("====Librarian Section=====")
                print("1. Book Management")
                print("2. Book Transactions")
                print("3. User Information")
                print("4. Return to main menu")

                ## Asking the user for input
                libraianchoice = input("Please choose between (1-4)")

                if libraianchoice == '1':

                    ##Printing the  menu
                    while True:
                        print("===========Book Management Section==========")
                        print("1. Add a book to the inventory")
                        print("2. Edit a book to the inventory")
                        print("3. Remove a book to the inventory")
                        print("4. Return to Librarian Menu")

                        ## Asking the user for input
                        bookChoice = input("Please choose between (1-4)")

                        if bookChoice == '1':
                            booktitle = input("Please enter the title of the book: ")
                            bookauthor = input("Please enter the author name: ")
                            bookgenre = input("Please enter the genre of the book: ")
                            bookISBN = int(input("Please enter the ISBN of the book: "))
                            bookquantity = int(input("Please enter the quantity "))
                            bookyear = int(input("Please enter the publication year"))
                            book1 = Book(booktitle, bookauthor, bookgenre, bookISBN, bookquantity, bookyear)
                            db.insert_book(book1)
                            print(f"{book1} added to the inventory.")

                        elif bookChoice == '2':
                            updatebookISBN = int(input("Please enter the ISBN of the book to update: "))
                            updatebooktitle = input("Please enter the updated title of the book: ")
                            updatebookauthor = input("Please enter the updated author name: ")
                            updatebookgenre = input("Please enter the updated genre of the book: ")
                            updatebookquantity = int(input("Please enter the updated quantity "))
                            updatebookyear = int(input("Please enter the updated publication year"))
                            db.update_book(updatebookISBN)
                            print(f"{updatebooktitle} updated to the inventory.")

                        elif bookChoice == '3':
                            deletebookISBN = int(input("Please enter the book ISBN to remove from the inventory"))
                            db.delete_book(deletebookISBN)

                            ## Prompting the user the returning to the main menu
                        elif bookChoice == '4':
                            print("returning to Librarian menu, Thank you.")
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")

                elif libraianchoice == '2':

                    ##Printing the  menu 
                    while True:
                        print("=========Book Trasactions==========")
                        print("1. Check Out a Book")
                        print("2. Check In a Book")
                        print("3. Return to Librarian Menu")

                        ## Asking the user for input
                        booktranschoice = input("Please enter your input between (1-3)")

                        if booktranschoice == '1':
                            checkUser = input("Please enter the username: ")
                            checkISBN = int(input("Please enter the ISBN of the book"))
                            duedatecheck = (input("Please enter the due date in YYYY-MM-DD format: "))
                            dateinput = datetime.strptime(duedatecheck, '%Y-%m-%d')
                            fixedstatus = "Checked Out"
                            duestatus = fixedstatus
                            trans1 = Transaction(checkUser, checkISBN, dateinput, duestatus)
                            db.check_out_book(trans1)
                            print("Entry recorded")


                        elif booktranschoice == '2':
                            checkUser = input("Please enter the username: ")
                            checkISBN = int(input("Please enter the ISBN of the book"))
                            duedatecheck = (input("Please enter the return date in YYYY-MM-DD format: "))
                            dateinput = datetime.strptime(duedatecheck, '%Y-%m-%d')
                            fixedstatus = "Returned"
                            duestatus = fixedstatus
                            trans1 = Transaction(checkUser, checkISBN, dateinput, duestatus)
                            db.check_in_book(trans1)


                        ## Prompting the user the returning to the main menu 
                        elif booktranschoice == '3':
                            print("returning to Librarian menu, Thank you.")
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")

                elif libraianchoice == '3':

                    ## printing the  menu  
                    while True:
                        print("====User Management=====")
                        print("1. Add a User record")
                        print("2. Update a User record")
                        print("3. Remove a User record")
                        print("4. Find User")
                        print("5. Return to Librarian Menu")

                        ## Asking the user for input
                        manageuserchoice = input("Please choose between (1-5)")

                        ## If the user wants to add a user information
                        if manageuserchoice == '1':
                            username = input("Please enter the User username: ")
                            password = input("Please enter the password")
                            name = input("Please enter the name")
                            contactInfo = input("please enter the contact information")
                            user1 = CommonUser(username, password, name, contactInfo)
                            db.insert_user(user1)
                            print(f"{user1} added to the storage.")


                        ## If the user wants to update the user information based on book username
                        elif manageuserchoice == '2':
                            updateUsername = input("Please enter the User username to update from the table")
                            updatedpassword = input("Please enter the updated password")
                            updatename = input("Please enter the update name: ")
                            updateContactinfo = input("Please enter the updated contact details")
                            db.update_user(updateUsername, updatedpassword, updatename, updateContactinfo)
                            print(f"{updateUsername} record is updated")

                            ## If the user wants to delete the user record
                        elif manageuserchoice == '3':
                            deleteusername = input("Please enter the User username to remove from the table")
                            db.delete_user(deleteusername)

                        elif usermenuchoice == '4':
                            findname = input("Please enter the name of the user to find")
                            db.filter_users_by_name(findname)

                            ## Prompting the user the returning to the main menu
                        elif manageuserchoice == '5':
                            print("returning to Librarian menu, Thank you.")
                            break

                            ## Prompting the user when an invalid input is given, and presents the menu again
                        else:
                            print("Invalid choice. Please enter a number between 1 and 4.")

                            ## Prompting the user the returning to the main menu
                elif libraianchoice == '4':
                    print("Returning to the Main menu, Thank you.!!")
                    break

                    ## Prompting the user when an invalid input is given, and presents the menu again
                else:
                    print("Invalid input entered, please choose between (1-4)")

        elif mainchoice == '3':
            ## printing the menu   
            while True:
                print("=======User Management=======")
                print("1. Search Books")
                print("2. Check Out Books")
                print("3. View Transaction History")
                print("4. Return to main menu")

                ## Asking the user for input
                usermenuchoice = input("Please choose between (1-4)")

                ## If the user wants to search the book based on book parameters
                if usermenuchoice == '1':
                    checkparameter = input("Please enter the book title, author, genre or ISBN")
                    findbook = checkparameter
                    db.search_books(findbook)

                    ## Entering the record into transactions table
                elif usermenuchoice == '2':
                    checkUser = input("Please enter the username: ")
                    checkISBN = int(input("Please enter the ISBN of the book"))
                    duedatecheck = (input("Please enter the return date in YYYY-MM-DD format: "))
                    dateinput = datetime.strptime(duedatecheck, '%Y-%m-%d')
                    fixedstatus = "Checked Out"
                    duestatus = fixedstatus
                    trans2 = Transaction(checkUser, checkISBN, dateinput, duestatus)
                    db.check_out_book(trans2)
                    print("Entry recorded")



                ## If the user wants to view the transaction history        
                elif usermenuchoice == '3':
                    viewUse = input("Please enter the username to view transactions: ")
                    db.view_transaction_history(viewUse)



                ## Prompting the user the returning to the main menu 
                elif usermenuchoice == '5':
                    print("Returning to main menu, Thank you..!!")
                    break


                ## Message prompt about invalid message and presents the menu again
                else:
                    print("Invalid input, please choose from (1-5)")

                    ## Prompting the user the end of program and exiting the console
        elif mainchoice == '4':
            print("Exiting program. Thank you!")
            break


        ## Prompting the user when an invalid input is given, and presents the menu again
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
