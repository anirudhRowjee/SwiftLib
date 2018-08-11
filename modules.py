import mysql.connector
from mysql.connector import Error
from python_mysql_dbconfig import read_db_config, read_pwd

# function to connect to the database


def connect(a):
    """ Connect to MySQL database """
    db_config = read_db_config()
    try:

        # print("Connecting to DB ...")
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            print('Connected to MySQL database')
        else:
            print('connection failed')

    except Error as e:
        print(e)

    # print('closing connection')
    # conn.close()


#   Defining library class. Will perform authentication and allow the user to continue,
#   else will exit when wrong password is provided


class Library:

    auth = False

    def __init__(self):

        pwd = read_pwd()
        password = input("Please enter the password >>> ")

        if password == pwd['pwd']:
            connect(1)
            print("welcome admin")
            self.auth = True


        else:
            print("Unauthorized user")
            self.auth = False
            exit()

    def auth_status(self):
        return self.auth


# create subclass / inherited class Book, which will have allow creation/deletion/query/search-sort-display of books

class Book(Library):

    def __init__(self):






