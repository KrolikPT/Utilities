#!/usr/bin/env python3
import os
import sys

##########################################################################################
# MODULES
##########################################################################################
from colors import colors
from file_creator import file_creator

##########################################################################################
# FUNCTIONS
##########################################################################################
def usage():
	print("\nUSAGE: python3 utls.py [-h <help>] [-i <install>] [-u <uninstall>] [-tc <terminal colors>] [-cf <Create File>]\n")


##########################################################################################
# COMMANDS
##########################################################################################
if len(sys.argv) == 2 and sys.argv[1] == "-h" or len(sys.argv) == 1:
	usage()
elif len(sys.argv) == 2 and sys.argv[1] == "-i":
	os.system("sudo cp utls.py /bin/utls")
	os.system("sudo cp colors.py /bin/colors.py")
	os.system("sudo cp file_creator.py /bin/file_creator.py")
	os.system("sudo chmod +x /bin/utls")
	print("Script installed!")
	print("Now you can use only: utls [OPTION]")
elif len(sys.argv) == 2 and sys.argv[1] == "-u":
	os.system("sudo rm /bin/utls")
	os.system("sudo rm /bin/colors.py")
	os.system("sudo rm /bin/file_creator.py")
	print("The script was removed!")
elif len(sys.argv) == 2 and sys.argv[1] == "-tc":
	colors()
elif len(sys.argv) == 2 and sys.argv[1] == "-cf":
    file_creator()
else:
	usage()
