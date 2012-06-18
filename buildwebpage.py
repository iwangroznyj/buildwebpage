#!/usr/bin/env python2
# encoding=utf8

import os, sys


def main(args):
	# check argument number
	if len(args) < 3:
		usage()
		return 0
	# get list of possible content files
	contentfiles = []
	for i in args[2:]:
		if isPrefixed(i, "c_"):
			contentfiles.append(i)
	if len(contentfiles) == 0:
		print args[0] + ": Error: no content files given"
		usage()
		return 0
	# read site template
	template = linesOfFile(args[1])
	# search for CONTENT line
	cl = 0
	for i in range(len(template)):
		if "CONTENT" in template[i]:
			cl = i
			break
	if cl == None:
		print args[0] + ": Error: template file has no CONTENT line"
		usage()
		return 0
	# replace CONTENT line by content file lines
	for name in contentfiles:
		content = linesOfFile(name)
		output = template[:cl] + content + template[cl+1:]
		saveFile(os.path.basename(name)[2:], output)
	return 0



def isPrefixed(name, prefix):
	"""checks if a file name starts with a given prefix"""
	fname = os.path.basename(name)
	if fname[:len(prefix)] == prefix:
		return True
	return False


def linesOfFile(name):
	"""reads a file linewise"""
	if not os.path.exists(name):
		print "Error: file", name, "not found."
		sys.exit(0)
	if not os.path.isfile(name):
		print "Error:", name, "is not a file."
		sys.exit(0)
	with open(name) as file:
		out = file.readlines()
	return out


def saveFile(name, content):
	"""saves lines to a file"""
	if os.path.exists(name):
		if not os.path.isfile(name):
			print "Error:", name, "is not a file."
			sys.exit(0)
		answer = raw_input("Warning: file '" + name + "' already exists, do you want to overwrite it? [y/N]:")
		if answer[0] != "y" and answer[0] != "Y":
			sys.exit(0)
	with open(name, "w") as file:
		file.truncate()
		file.writelines(content)

def usage():
	"""prints help message"""
	print "usage:"
	print " ", sys.argv[0], "template_file content_file [additional content files]"
	print "description:"
	print "  This script generates a static website by inserting the content of a series"
	print "  of html files into a template."
	print "conventions:"
	print " *the template file must contain a line only consisting of whitespace and the"
	print "  word CONTENT in capital letters.  This is where the content will be inserted."
	print " *the content files must be prefixed with \"c_\""


if __name__ == "__main__":
	sys.exit(main(sys.argv))

