#!/usr/bin/env python3
import os
import sys
import tabulate
import pandas as pd

##########################################################################################
# FUNCTIONS
##########################################################################################
def usage():
	print("\nUSAGE: python3 utls.py [-h <help>] [-tc <terminal colors>] [-is <If Statements>]\n")


def colors():
	d = "\033[0m"           # default
	bk = "\033[1;30m"       # black
	r = "\033[1;31m"        # red
	g = "\033[1;32m"        # green
	y = "\033[1;33m"        # yellow
	b = "\033[1;34m"        # blue
	m = "\033[1;35m"        # magenta
	c = "\033[1;36m"        # cyan
	w = "\033[1;37m"        # white

	cores = {"1": ["Color", "Default", bk + "Black" + d, r + "Red" + d, g + "Green" + d, y + "Yellow" + d, b + "Blue" + d, m + "Magenta" + d, c + "Cyan" + d, w + "White" + d],
         "2": ["Foreground Code", "\\033[0m", bk + "\\033[1;30m" + d, r + "\\033[1;31m" + d, g + "\\033[1;32m" + d, y + "\\033[1;33m" + d, b + "\\033[1;34m" + d, m + "\\033[1;35m" + d, c + "\\033[1;36m" + d, w + "\\033[1;37m" + d],
         "3": ["Background Code", "0", bk + "40" + d, r + "41" + d, g + "42" + d, y + "43" + d, b + "44" + d, m + "45" + d, c + "46" + d, w + "47" + d]
	}

	df = pd.DataFrame(cores)

	print("\n###############################################")
	print("############### TERMINAL COLORS ###############")
	print("###############################################")

	print("%s\n" % tabulate.tabulate(df, tablefmt="grid", showindex=False))

	print("Example: echo \"\\033[1;31mSample Text\\033[0m\"\n")


def if_statements():
	print("\n-eq // Equal")
	print("-ne // Not equal")
	print("$# // Number of args")
	print("$1 // First argument of command")
	print("-ge // Greater or equal")
	print("-le // Less or equal")
	print("-gt // Greater than")
	print("-lt // Less than")
	print("$var =~ [^0-9] // Check if value is a number\n")


##########################################################################################
# COMMANDS
##########################################################################################
if len(sys.argv) == 2 and sys.argv[1] == "-h" or len(sys.argv) == 1:
	usage()
elif len(sys.argv) == 2 and sys.argv[1] == "-tc":
	colors()
elif len(sys.argv) == 2 and sys.argv[1] == "-is":
    if_statements()
else:
	usage()
