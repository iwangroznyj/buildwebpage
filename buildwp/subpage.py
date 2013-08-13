'''Classes for representing subpages of a webpage.'''


import re
import markdown
from . import cfg
from . import warning


# Precompile regexes
RE_TITLE = re.compile(cfg.RE_SUBPG_TITLE, re.UNICODE | re.IGNORECASE)
RE_MENU = re.compile(cfg.RE_SUBPG_MENU, re.UNICODE | re.IGNORECASE)
RE_MARKDOWN = re.compile(cfg.RE_MARKDOWN, re.UNICODE | re.IGNORECASE)


def read_subpagefile(filename):
    '''Open subpage from file.

    :param filename: name of the subpage file
    :type  filename: str
    :return:         subpage on success; None on failure
    :rtype:          Subpage / NoneType

    '''
    with open(filename) as fileptr:
        try:
            content = str(fileptr.read(), cfg.INPUTENC)
        except IOError as error:
            warning.warnf(str(error))
            return None
    return Subpage(content, filename)


class Subpage(object):
    '''Representation of a html subpage.'''

    def __init__(self, content, filename=None):
        '''Create a subpage.

        :param content:  content of the subpage
        :type  content:  unicode
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
        :rtype:  unicode

        '''
        if self.is_markdown:
            return markdown.markdown(self.content,
                                     output_format=cfg.DEFAULT_HTMLFORMAT)
        else:
            return self.content
