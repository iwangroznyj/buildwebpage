'''Classes for representing subpages of a webpage.'''


import re
import markdown
from . import cfg


# Precompile regexes
RE_TITLE = re.compile(cfg.RE_SUBPG_TITLE, re.UNICODE | re.IGNORECASE)
RE_MENU = re.compile(cfg.RE_SUBPG_MENU, re.UNICODE | re.IGNORECASE)


class Subpage(object):
    '''Representation of a html subpage.'''

    def __init__(self, content, filename=None):
        '''Create a subpage.

        :param content:  content of the subpage
        :type  content:  unicode
        :param filename: name of the subpage file (for later reference)
        :type  filename: str

        '''
        self.content = content
        self.filename = ''
        if filename:
            self.filename = filename
        self.has_title = False
        self.title = ''
        self.has_menu = False
        self.menu = ''
        match = RE_TITLE.search(content)
        if match:
            self.title = match.group(1)
            self.has_title = True
        match = RE_MENU.search(content)
        if match:
            self.menu = match.group(1)
            self.has_menu = True

    def get_html(self):
        '''Return content of the subpage (assuming it's html).

        :return: html code
        :rtype:  unicode

        '''
        return self.content


class MarkdownSubpage(Subpage):
    '''Representation of a markdown subpage.'''

    def get_html(self):
        '''Convert markdown into html.

        :return: html code
        :rtype:  unicode

        '''
        return markdown.markdown(self.content,
                                 output_format=cfg.DEFAULT_HTMLFORMAT)
