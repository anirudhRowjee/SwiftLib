# MODULES PAGE, ALL IMPOPRANT APP-CRITICALS HERE

# import mysql ops and reader for db info

import mysql.connector
from python_mysql_dbconfig import read_db_config


db_config = read_db_config()

# create a connector and connect to the database

cnx = mysql.connector.connect(**db_config)

# if db connection successful, proceed. Else, kill application.

if cnx.is_connected():
    # print('Connected to MySQL database')
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
            print("WELCOME", uname.upper())
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
    def __init__(self):
        print("Book Created!")

class member:
    def __init__(self):
        print("Member Created!")

class issue:
    def __init__(self):
        print("Issued!")








