#!/usr/bin/env python


__author__ = 'Johannes Englisch'


import os
import sys
import glob
import re


# replacement settings
file_prefix = '_'
destination = '../'
template_file = 'template.html'
content_string = '<!-- content -->'
begin_title = '<!-- begin title -->'
end_title = '<!-- end title -->'
begin_menu = '<!-- begin menuid -->'
end_menu = '<!-- end menuid -->'


# regexes
re_titletag = re.compile('{0}.*{1}'.format(begin_title, end_title))
re_title = re.compile('{0}(.*){1}'.format(begin_title, end_title))
re_menutag = re.compile('{0}.*{1}'.format(begin_menu, end_menu))
re_menu = re.compile('{0}(.*){1}'.format(begin_menu, end_menu))


class Template:
	'''template class

	filename:		name of the template file (string)
	content:		content of the template (string)
	'''

	def __init__(self, filename):
		self.filename = filename
		with open(filename) as file:
			self.content = file.read()
		if content_string not in self.content:
			raise RuntimeError('Template file \'{0}\' must contain \'{1}\''.format(filename, content_string))


class Webpage:
	'''subpage class

	filename:		name of the webpage file (string)
	template:		template where content ins inserted (Template)
	content:		subpage content (string)
	title:			title (string)
	menuentry:		menu entry of this content
	webpage:		webpage built from template (string)
	'''

	def __init__(self, filename, template):
		self.filename = filename
		self.template = template
		with open(filename) as file:
			self.content = file.read()
		self.title = re_title.findall(self.content)[0]
		self.content = re_titletag.sub('', self.content)
		self.menuentry = re_menu.findall(self.content)[0]
		self.content = re_menutag.sub('', self.content)
		self.__build()

	def __build(self):
		webpage = self.template.content
		webpage = webpage.replace(content_string, self.content)
		webpage = re_titletag.sub(self.title, webpage)
		menu = re_menu.findall(webpage)
		webpage = re.sub('<([^>]*?id=["\']{0}[\'"][^>]*?)>'.format(
			self.menuentry), r'<\1 class="menu-current">', webpage)
		self.webpage = webpage

	def __str__(self):
		return self.webpage


def main(args):
	if len(args) > 1:
		subpages = args[1:]
	else:
		subpages = glob.glob('{0}*'.format(file_prefix))
	template = Template(template_file)
	for file_name in subpages:
		page = Webpage(file_name, template)
		file_base = os.path.basename(file_name)
		if file_prefix in file_base:
			file_base = file_base[len(file_prefix):]
		new_file = os.path.join(destination, file_base)
		print 'Merging {subpage} and {template} to {webpage}.'.format(
				subpage = file_name,
				template = template_file,
				webpage = new_file)
		with open(new_file, 'w') as file:
			file.write(str(page))


if __name__ == "__main__":
	main(sys.argv)


