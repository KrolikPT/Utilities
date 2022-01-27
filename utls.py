#!/usr/bin/env python3
import os
import sys

##########################################################################################
# MODULES
##########################################################################################
from colors import colors
from file_creator import file_creator
import installation

##########################################################################################
# FUNCTIONS
##########################################################################################
def usage():
	print("\nUsage: python3 utls.py [-h <help>] [-i <install/update>] [-u <uninstall>] [-tc <terminal colors>] [-cf <Create File>]\n")


##########################################################################################
# COMMANDS
##########################################################################################
if len(sys.argv) == 2 and sys.argv[1] == "-h" or len(sys.argv) == 1:
	usage()
elif len(sys.argv) == 2 and sys.argv[1] == "-i":
	install()	
elif len(sys.argv) == 2 and sys.argv[1] == "-u":
	uninstall()
elif len(sys.argv) == 2 and sys.argv[1] == "-tc":
	colors()
elif len(sys.argv) == 2 and sys.argv[1] == "-cf":
    file_creator()
else:
	usage()
