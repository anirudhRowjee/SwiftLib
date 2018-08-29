# MODULES PAGE, ALL IMPORTANT APP-CRITICAL STUFF HERE

# import mysql ops and reader for db info

import mysql.connector
from mysql.connector import Error
# import error from mysql.connector
from python_mysql_dbconfig import read_db_config
from tabulate import tabulate
import datetime


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

        name = input("Please Enter the NAME of the BOOK >>> ").upper()
        author = input("Please Enter the NAME of the AUTHOR >>> ").upper()
        isbn = int(input("Please Enter the ISBN of the BOOK >>> "))
        price = int(input("Please Enter the PRICE of the BOOK >>> "))
        collection = input("Please Enter the name of the PARENT COLLECTION of the BOOK (type none if no parent coll exists) >>> ").upper()
        rent_amt = int(input("Please Enter the DAILY RENT AMOUNT of the BOOK >>> "))
        genre = input("Please Enter the GENRE of the BOOK >>> ").upper()

        cur = cnx.cursor()

        q1 = "INSERT INTO books (name, author, price, collection, rent_amt, genre, isbn) VALUES "
        q2 = "('"+name+"', '"+author+"', "+str(price)+", '"+collection+"', "+str(rent_amt)+", '"+genre+"', "+str(isbn)+")"
        q = q1 + q2
        #print(q)
        try:
            cur.execute(q)
            cnx.commit()
            s = "BOOK <<<" + name + ">>> BY <<<" + author + ">>> HAS BEEN ADDED!"
            print(s)
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
        s = True
        while s:
            print("\nBOOK OPEPRATIONS")
            c = int(input("1 to create a new book, 2 to delete a book, 3 to show all, 4 to leave BOOK OPERATIONS >>> "))
            if c == 1:
                self.create_book()
            if c == 2:
                self.delete_book()
            if c == 3:
                self.show_all()
            if c == 4:
                s = False



class member:

    def create_member(self):
        name = input("Please enter the NAME of the MEMBER >>> ").upper()
        date_of_membership = str(datetime.date.today())
        email = input("Please Enter the EMAIL ID of the MEMBER >>> ").upper()
        phno = int(input("Plese enter the PHONE NUMBER of the MEMBER >>> "))
        q1 = "INSERT INTO members (name, date_of_membership, email, phno)"
        q2 = "VALUES ('"+name+"','"+date_of_membership+"','"+email+"',"+str(phno)+")"
        q = q1 + q2
        cur = cnx.cursor()
        try:
            cur.execute("USE libmgmt")
            cur.execute(q)
            cnx.commit()
            s = "\nMEMBER <<<" + name + ">>> HAS BEEN ADDED!"
            print(s)
        except Error as e:
            print(e)
        try:
            z = "select * from members where name='" + name + "';"
            cur.execute(z)
            p = cur.fetchall()
            print(tabulate(p,headers=["MEMBER ID", "NAME", "DATE OF MEMBERSHIP", "LOST", "EMAIL", "PHONE NUMBER", "HAS BORROWED"],tablefmt="grid"))
        except Error as e:
            print(e)
        print("\n******************PLEASE REMEMBER MEMBER ID*************************\n")


    def show_all(self):
        cur = cnx.cursor()
        try:
            cur.execute("use libmgmt")
            cur.execute('select * from members')
        except Error as e:
            print(e)
        z = cur.fetchall()
        print(tabulate(z, headers=["MEMBER ID", "NAME", "DATE OF MEMBERSHIP", "LOST", "EMAIL", "PHONE NUMBER",
                                   "HAS BORROWED"], tablefmt="grid"))

    def delete_member(self):
            cur = cnx.cursor()
            x = int(input("Please Enter Member ID of Member to be deleted >>> "))
            s = 'SELECT name FROM members WHERE id=' + str(x)
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

            choice = input("ARE YOU SURE YOU WANT TO DELETE MEMBER " + name + "? (y/n)")
            if choice == "y":

                q = 'DELETE FROM members WHERE id=' + str(x)

                try:
                    cur.execute("use libmgmt")
                    cur.execute(q)
                    cnx.commit()
                except Error as e:
                    print(e)
                print("Member Successfuly Deleted")

            if choice == "n":
                print("PLEASE BE SURE NEXT TIME")


    def __init__(self):
        s = True
        while s:
            print("\nMEMBER OPEPRATIONS")
            c = int(input("1 to create a new member, 2 to delete a member, 3 to show all members, 4 to leave MEMBER OPERATIONS >>> "))
            if c == 1:
                self.create_member()
            if c == 2:
                self.delete_member()
            if c == 3:
                self.show_all()
            if c == 4:
                s = False


class issue:

    def issue_book(self):

        n1 = input("\nplease enter FULL NAME of the USER wishing to BORROW >>> ")
        n_o1 = "%"+n1.upper()+"%"
        cur = cnx.cursor()
        q = "select id from members where name like '" + n_o1 + "'"
        try:
            cur.execute("use libmgmt")
            cur.execute(q)
            id_o = str(cur.fetchall())
            id = ""
            for i in id_o:
                if i.isdigit():
                    id = id + i
            id = int(id)
            # print("MEMBER ID >> ", id)

        except Error as e:
            print(e)

        m_id = id

        n2 = input("please enter FULL NAME of the BOOK to be BORROWED >>> ")
        n_o2 = "%" + n2.upper() + "%"
        cur = cnx.cursor()
        q = "select id from books where name like '" + n_o2 + "'"
        try:
            cur.execute("use libmgmt")
            cur.execute(q)
            id_o = str(cur.fetchall())
            id = ""
            for i in id_o:
                if i.isdigit():
                    id = id + i
            id = int(id)
            # print("BOOK ID >> ", id)
        except Error as e:
            print(e)

        b_id = id

        s = str(datetime.date.today())

        q1 = "INSERT INTO issue (book_id, member_id, date_issued) VALUES "
        q2 = "("+str(b_id)+", "+str(m_id)+",'"+s+"')"
        q = q1+q2
        # print(q)

        try:
            cur.execute("use libmgmt")
            cur.execute(q)
            cnx.commit()
            stringd = "\nBOOK <<<" + n2 + ">>> HAS BEEN ISSUED TO MEMBER <<<" + n1 + ">>> SUCCESSFULLY"
            print(stringd)
        except Error as e:
            print(e)


    def show_all(self):
        cur = cnx.cursor()
        try:
            cur.execute("use libmgmt")
            s1 = 'select issue.id, books.name, members.name, issue.date_issued, issue.return_status, issue.lost, issue.date_returned, issue.amt_tbc, issue.amt_collected  '
            s2 = 'from issue, members, books where issue.book_id = books.id and issue.member_id = members.id'
            s = s1 + s2
            cur.execute(s)
        except Error as e:
            print(e)
        z = cur.fetchall()
        print(tabulate(z, headers=["ISSUE ID", "BOOK NAME", "MEMBER NAME", "DATE ISSUED", "STATUS", "LOST",
                                   "DATE RETURNED", "AMOUNT TO BE COLLECTED", "AMOUNT COLLECTED"], tablefmt="grid"))


    def return_book(self):

        n1 = input("\nplease enter FULL NAME of the USER wishing to RETURN BOOK >>> ")
        n_o1 = "%" + n1.upper() + "%"
        cur = cnx.cursor()
        q = "select id from members where name like '" + n_o1 + "'"
        try:
            cur.execute("use libmgmt")
            cur.execute(q)
            id_o = str(cur.fetchall())
            id = ""
            for i in id_o:
                if i.isdigit():
                    id = id + i
            id = int(id)
            # print("MEMBER ID >> ", id)

        except Error as e:
            print(e)

        m_id = id

        n2 = input("please enter FULL NAME of the BOOK to be RETURNED >>> ")
        n_o2 = "%" + n2.upper() + "%"
        cur = cnx.cursor()
        q = "select id from books where name like '" + n_o2 + "'"
        try:
            cur.execute("use libmgmt")
            cur.execute(q)
            id_o = str(cur.fetchall())
            id = ""
            for i in id_o:
                if i.isdigit():
                    id = id + i
            id = int(id)
            # print("BOOK ID >> ", id)
        except Error as e:
            print(e)

        b_id = id

        s = str(datetime.date.today())

        q1 = "update issue set return_status = 'Returned', date_returned='"+s+"' where "
        q2 = "member_id = "+str(m_id) + " and book_id="+str(b_id)
        q = q1 + q2

        try:
            cur.execute("use libmgmt")
            cur.execute(q)
            cnx.commit()
            stringd = "\nBOOK <<<" + n2 + ">>> HAS BEEN RETURNED BY MEMBER <<<" + n1 + ">>> SUCCESSFULLY"
            print(stringd)
        except Error as e:
            print(e)



    def __init__(self):
        s = True
        while s:
            print("\nISSUE OPERATIONS")
            c = int(input("1 to issue a book, 2 to return a book, 3 to view all history and 4 to leave ISSUE OPERATIONS >>> "))
            if c == 1:
                self.issue_book()
            if c == 2:
                self.return_book()
            if c == 3:
                self.show_all()
            if c == 4:
                s = False








