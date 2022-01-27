import os

FILENAME = ""
EXTENSION = ""

def permission():
    os.system("sudo chmod +x %s.%s" % (FILENAME, EXTENSION))


def file_creator():
    print("\n#####################################################")
    print("#################### CREATE FILE ####################")
    print("#####################################################")
    print("# What type of file you want create?")
    print("# 1 ) - Bash")
    print("# 2 ) - Python2")
    print("# 3 ) - Python3")
    print("# 4 ) - Text")
    print("# 0 ) - Exit")
    print("#####################################################")
    option = input("# Option: ")

    FILENAME = input("# Filename (without extension): ")

    if option == "1":
        
        EXTENSION = ".sh"

        with open(FILENAME + EXTENSION, "w") as f:
            f.write("#!/bin/bash\n")

    elif option == "2":

        EXTENSION = ".py"
        
        with open(FILENAME + EXTENSION, "w") as f:
            f.write("#!/usr/bin/env python\n")

    elif option == "3":

        EXTENSION = ".py"

        with open(FILENAME + EXTENSION, "w") as f:
            f.write("#!/usr/bin/env python3\n")

    elif option == "4":

        EXTENSION = ".txt"
        
        with open(FILENAME + EXTENSION, "w") as f:
            f.write("")

    elif option == "0":
        quit()

    else:
        print("Invalid Option")

    permission()