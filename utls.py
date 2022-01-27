#!/usr/bin/env python3
import os
import sys

# Modules
from colors import colors
from file_creator import file_creator

##########################################################################################
# FUNCTIONS
##########################################################################################
def usage():
	print("\nUSAGE: python3 utls.py [-h <help>] [-tc <terminal colors>] [-cf <Create File>]\n")


##########################################################################################
# COMMANDS
##########################################################################################
if len(sys.argv) == 2 and sys.argv[1] == "-h" or len(sys.argv) == 1:
	usage()
elif len(sys.argv) == 2 and sys.argv[1] == "-tc":
	colors()
elif len(sys.argv) == 2 and sys.argv[1] == "-cf":
    file_creator()
else:
	usage()
