#!/usr/bin/env python3
import os
from terminal_colors import colors
import sys

def usage():
	print("\nUSAGE: python3 utls.py [-h <help>] [-cc <terminal color codes>]\n")


if len(sys.argv) == 2 and sys.argv[1] == "-h" or len(sys.argv) == 1:
	usage()
elif len(sys.argv) == 2 and sys.argv[1] == "-cc":
	colors()
else:
	usage()
