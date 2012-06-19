#!/usr/bin/env python2
# encoding=utf8

import os
import sys


def main(args):
	# Argument handling
	if len(args) < 3:
		usage()
		return 0
	# Check for subpage files
	subpages = []
	for i in args[2:]:
		if isPrefixed(i, "c_"):
			subpages.append(i)
	if not subpages:
		error("no subpage files given", True)
	# Read template
	template = readFile(args[1])
	# Check for CONTENT
	if not 'CONTENT' in template:
		error("template file lacks the word CONTENT in capital letters", True)
	# Replace CONTENT by subpages
	for name in subpages:
		content = readFile(name)
		output = template.replace('CONTENT', content)
		saveFile(os.path.basename(name)[2:], output)
	return 0


def isPrefixed(name, prefix):
	""" checks if a file name starts with a given prefix """
	fname = os.path.basename(name)
	if fname.startswith(prefix):
		return True
	return False


def readFile(name):
	""" reads a file and return its content as a string """
	if not os.path.exists(name):
		error(name + " not found")
	if not os.path.isfile(name):
		error(name + " is not a file")
	with open(name) as file:
		out = file.read()
	return out


def saveFile(name, content):
	""" saves lines to a file """
	if os.path.exists(name):
		if not os.path.isfile(name):
			error(name + " is not a file")
		answer = raw_input("Warning: file '" + name + "' already exists, do you want to overwrite it? [y/N]:")
		if answer[0] != "y" and answer[0] != "Y":
			sys.exit(0)
	with open(name, "w") as file:
		file.truncate()
		file.write(content)

def usage():
	""" prints help message """
	print "usage:"
	print " ", sys.argv[0], "template_file content_file [additional content files]"
	print "description:"
	print "  This script generates a static website by inserting the content of a series"
	print "  of html files into a template."
	print "conventions:"
	print " *the template file must contain a line only consisting of whitespace and the"
	print "  word CONTENT in capital letters.  This is where the content will be inserted."
	print " *the content files must be prefixed with \"c_\""


def error(message="unexpected error", showusage=False):
	""" prints error message and terminates """
	print sys.argv[0] + ": Error: " + message
	if showusage:
		usage()
	sys.exit(0)


if __name__ == "__main__":
	sys.exit(main(sys.argv))


