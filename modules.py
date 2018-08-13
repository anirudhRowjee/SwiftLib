# MODULES PAGE, ALL IMPORTANT APP-CRITICAL STUFF HERE

# import mysql ops and reader for db info

import mysql.connector
from mysql.connector import Error
# import error from mysql.connector
from python_mysql_dbconfig import read_db_config
from tabulate import tabulate


db_config = read_db_config()

# create a connector and connect to the database

cnx = mysql.connector.connect(**db_config)

# if db connection successful, proceed. Else, kill application.

if cnx.is_connected():
    print('Connected to MySQL database')
    pass
else:
    print('connection failed')
    exit()

#   Defining library class. Will perform authentication and allow the user to continue,
#   else will exit when wrong password is provided


class Library:

    auth = False

    def __init__(self):

        # take username and password as input

        uname = input("Please enter username >>> ")
        password = input("Please enter the password >>> ")

        # now that we have username and password, we can create a query to find password based on username

        op_cur = cnx.cursor()       # create a cursor to run password query

        q = "SELECT pwd FROM users WHERE username = '" + uname + "'"

        # now that query has been created, we can execute it

        op_cur.execute(q)
        pwd_find = op_cur.fetchone()

        # query executes, and output is stored in pwd_find

        pwd = ""
        for i in str(pwd_find):
            if i.isalnum():
                pwd = pwd + i

        # format pwd_find by creating new string pwd and removing all brackets/non alphanumerics

        if pwd == password:
            print("\nWELCOME", uname.upper())
            self.auth = True
            # verified user, can continue to use application
        else:
            print("BAD AUTH")
            self.auth = False
            exit()
            # unverified user, application access is cut off immediately

    def auth_status(self):
        return self.auth


# create subclass / inherited class Book, which will have allow creation/deletion/query/search-sort-display of books


class book:

    def create_book(self):

        # take all information about the book from user

        name = input("Please Enter the NAME of the BOOK >>> ")
        author = input("Please Enter the NAME of the AUTHOR >>> ")
        isbn = int(input("Please Enter the ISBN of the BOOK >>> "))
        price = int(input("Please Enter the PRICE of the BOOK >>> "))
        collection = input("Please Enter the name of the PARENT COLLECTION of the BOOK (type none if no parent coll exists) >>> ")
        rent_amt = int(input("Please Enter the DAILY RENT AMOUNT of the BOOK >>> "))
        genre = input("Please Enter the GENRE of the BOOK >>> ")

        cur = cnx.cursor()

        q1 = "INSERT INTO books (name, author, price, collection, rent_amt, genre, isbn) VALUES "
        q2 = "('"+name+"', '"+author+"', "+str(price)+", '"+collection+"', "+str(rent_amt)+", '"+genre+"', "+str(isbn)+")"
        q = q1 + q2
        #print(q)
        try:
            cur.execute(q)
            cnx.commit()
        except Error as e:
            print(e)

    def show_all(self):
        cur = cnx.cursor()
        try:
            cur.execute("use libmgmt")
            cur.execute('select * from books')
        except Error as e:
            print(e)

        z = cur.fetchall()
        print("\n")
        print(tabulate(z,headers=["ID","NAME", "AUTHOR", "PRICE", "COLLECTION", "STATUS", "DAILY RENT", "GENRE", "ISBN"],tablefmt="grid"))

    def delete_book(self):
        cur = cnx.cursor()
        x = int(input("Please Enter ISBN of book to be deleted >>> "))
        s = 'SELECT name FROM books WHERE isbn='+str(x)
        # print(s)
        try:
            cur.execute("use libmgmt")
            cur.execute(s)
        except Error as e:
            print(e)

        n = cur.fetchone()
        name = ""

        for i in str(n):
            if i.isalnum() == True or i == "'" or i == " ":
                name = name + i

        choice = input("ARE YOU SURE YOU WANT TO DELETE BOOK " +  name + "? (y/n)")
        if choice == "y":

            q = 'DELETE FROM books WHERE isbn='+str(x)

            try:
                cur.execute("use libmgmt")
                cur.execute(q)
                cnx.commit()
            except Error as e:
                print(e)
            print("Book Successfuly Deleted")

        if choice == "n":
            print("PLEASE BE SURE NEXT TIME")


    def __init__(self):
        print("\nBOOK OPEPRATIONS")
        c = int(input("1 to create a new book, 2 to delete a book, 3 to show all >>> "))
        if c == 1:
            self.create_book()
        if c == 2:
            self.delete_book()
        if c == 3:
            self.show_all()



class member:
    def __init__(self):
        print("Member Created!")

class issue:
    def __init__(self):
        print("Issued!")








