# program to run a library

import modules as libmaster

lib = libmaster.Library()

print("SwiftLib v1.0")

while lib.auth_status() == True:

    x = int(input("\nPress 1 for CRUD on books, 2 for CRUD on members, 3 to issue books, 4 to exit >>> "))

    if x == 1:
        libmaster.book()

    if x == 2:
        libmaster.member()

    if x == 3:
        libmaster.issue()

    if x == 4:

        c = input("\nAre you sure you want to exit? (y/n) >>> ")

        if c == 'y':

            print("\nThank you for using SwiftLib!")
            exit()

        if c == 'n':
            continue










