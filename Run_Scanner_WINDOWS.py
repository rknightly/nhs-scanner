#!/usr/bin/python

from src.id_reader import main
import os
import sys


if __name__ == '__main__':
	# Change the directory to the location of the file
	# Otherwise the program runs from home directory
	os.chdir(sys.path[0])

	main()
