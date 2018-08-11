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

    if a == 0:
        print('closing connection')
        conn.close()


#


class Library:

    def __init__(self):
        pwd = read_pwd()
        password = input("Please enter the password >>> ")
        if password == pwd['pwd']:
            print("welcome admin")
            connect(1)
        else:
            print("Unauthorized user")
            exit()

class Book(Library):

    def __init__(self):
        o = int(input("Enter 1 to create, 2 to remove"))
        if o == 1:
            print("Book created")
        if o == 2:
            print("Book Deleted")


