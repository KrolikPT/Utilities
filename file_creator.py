def filename():
    name = input("# Filename (without extension): ")
    return name

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

    if option == "1":
        
        with open(filename() + ".sh", "w") as f:
            f.write("#!/bin/bash\n")

    elif option == "2":
        
        with open(filename() + ".py", "w") as f:
            f.write("#!/usr/bin/env python\n")

    elif option == "3":

        with open(filename() + ".py", "w") as f:
            f.write("#!/usr/bin/env python3\n")

    elif option == "4":
        
        with open(filename() + ".txt", "w") as f:
            f.write("")

    elif option == "0":
        quit()

    else:
        print("Invalid Option")