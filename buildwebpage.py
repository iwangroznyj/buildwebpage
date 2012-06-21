#!/usr/bin/env python2

import os
import sys

FILEPREFIX="_"
CONTENTSTRING="<!--CONTENT-->"
OUTPUTDIR="../"


def main(args):
	# Argument handling
	if len(args) < 3:
		usage()
		return 0
	# Check for subpage files
	subpages = [ i for i in args[2:] if os.path.basename(i).startswith(FILEPREFIX) ]
	if not subpages:
		raise RuntimeError("no subpage files given")
	# Read template
	template = readFile(args[1])
	# Check for content string
	if not CONTENTSTRING in template:
		raise RuntimeError("template file lacks the word CONTENT in capital letters")
		# TODO edit error message
	# Replace content string by subpages
	for name in subpages:
		content = readFile(name)
		output = template.replace(CONTENTSTRING, content)
		outfile = OUTPUTDIR + os.path.basename(name)[len(FILEPREFIX):]
		saveFile(outfile, output)
	return 0


def readFile(name):
	""" reads a file and return its content as a string """
	with open(name) as file:
		out = file.read()
	return out


def saveFile(name, content):
	""" saves lines to a file """
	if os.path.exists(name):
		answer = raw_input("Warning: file '" + name + "' already exists, do you want to overwrite it? [y/N]:")
		if answer[0].lower() != "y":
			return
	with open(name, "w") as file:
		file.write(content)

def usage():
	""" prints help message """
	# TODO adapt usage string
	print "usage:"
	print "  " + sys.argv[0] + " template subpages ..."
	print ""
	print "  Generate a static website by inserting the content of a series of subpages"
	print "  into a template."
	print ""
	print "  The template file must contain the word CONTENT in capital letters which will"
	print "  be replaced by the content of the subpages."
	print ""
	print "  The file names of the subpages must be prefixed with '" + PREFIX +"' to be recognised by"
	print "  the script."


def error(message="unexpected error", showusage=False):
	""" prints error message and terminates """
	print sys.argv[0] + ": Error: " + message
	if showusage:
		usage()
	sys.exit(0)


if __name__ == "__main__":
	sys.exit(main(sys.argv))


