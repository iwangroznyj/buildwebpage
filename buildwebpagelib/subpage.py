import re
import markdown
import glob

from os.path import join, basename

from . import cfg
from . import warning

__all__ = ['read_subpages', 'Subpage']


# Precompile regexes
RE_TITLE = re.compile(cfg.RE_SUBPG_TITLE, re.UNICODE | re.IGNORECASE)
RE_MENU = re.compile(cfg.RE_SUBPG_MENU, re.UNICODE | re.IGNORECASE)
RE_MARKDOWN = re.compile(cfg.RE_MARKDOWN, re.UNICODE | re.IGNORECASE)


def read_subpages(folder, blacklist=()):
    for filename in glob.iglob(join(folder, '*')):
        if basename(filename) in blacklist:
            continue
        try:
            with open(filename, encoding='utf-8') as f:
                yield Subpage(f.read(), filename)
        except IOError as error:
            warning.warnf('Could not read {}'.format(filename))
            warning.warnf(error)


class Subpage(object):
    '''Representation of a html subpage.'''

    def __init__(self, content, filename=None):
        '''Create a subpage.

        :param content:  content of the subpage
        :type  content:  str
        :param filename: name of the subpage file
        :type  filename: str

        '''
        self.filename = ''
        self.content = content
        self.has_title = False
        self.has_menu = False
        self.is_markdown = False
        self.title = ''
        self.menu = ''
        if filename:
            self.filename = filename
        self._parse_comments()

    def _parse_comments(self):
        '''Parse comments found in the subpage.'''
        match = RE_TITLE.search(self.content)
        if match:
            self.title = match.group(1)
            self.has_title = True
            self.content = self.content.replace(match.group(0), '')
        match = RE_MENU.search(self.content)
        if match:
            self.menu = match.group(1)
            self.has_menu = True
            self.content = self.content.replace(match.group(0), '')
        match = RE_MARKDOWN.search(self.content)
        if match:
            self.is_markdown = True
            self.content = self.content.replace(match.group(0), '')

    def get_html(self):
        '''Return content of the subpage in html

        :return: html code
        :rtype:  str

        '''
        if self.is_markdown:
            return markdown.markdown(self.content,
                                     output_format=cfg.DEFAULT_HTMLFORMAT)
        else:
            return self.content
