#!/usr/bin/env python2

import os
import sys
import glob

FILEPREFIX="_"
TEMPLATE="template.html"
CONTENTSTRING="<!--CONTENT-->"
OUTPUTDIR="../"


def main(args):
	if len(args) < 2:
		subpages = glob.glob(FILEPREFIX + '*')
	else:
		subpages = args[2:]
	if not subpages:
		raise RuntimeError("No subpage files given")
	with open(glob.glob(TEMPLATE)) as file:
		template = file.read()
	if not CONTENTSTRING in template:
		raise RuntimeError("Template file lacks the substitution string '" + CONTENTSTRING + "'")
	for name in subpages:
		with open(name) as file:
			content = file.read()
		output = template.replace(CONTENTSTRING, content)
		outfile = OUTPUTDIR + os.path.basename(name)[len(FILEPREFIX):]
		saveFile(outfile, output)
	return 0


def saveFile(name, content):
	""" saves lines to a file """
	if os.path.exists(name):
		answer = raw_input("Warning: file '" + name + "' already exists, do you want to overwrite it? [y/N]:")
		if answer[0].lower() != "y":
			return
	with open(name, "w") as file:
		file.write(content)


if __name__ == "__main__":
	sys.exit(main(sys.argv))


