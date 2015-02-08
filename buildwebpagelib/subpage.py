import re

from glob import iglob
from os.path import join, basename
from markdown import markdown

from . import cfg
from . import warning

__all__ = ['read_subpages', 'Subpage']


# Precompile regexes
RE_TITLE = re.compile(cfg.RE_SUBPG_TITLE, re.UNICODE | re.IGNORECASE)
RE_MENU = re.compile(cfg.RE_SUBPG_MENU, re.UNICODE | re.IGNORECASE)
RE_MARKDOWN = re.compile(cfg.RE_MARKDOWN, re.UNICODE | re.IGNORECASE)


def read_subpages(folder, blacklist=()):
    for filename in iglob(join(folder, '*')):
        if basename(filename) in blacklist:
            continue
        try:
            with open(filename, encoding='utf-8') as f:
                yield Subpage(f.read(), filename)
        except IOError as error:
            warning.warnf('Could not read {}'.format(filename))
            warning.warnf(error)


class Subpage(object):

    def __init__(self, content, filename=None):
        self.content = content
        self.filename = ''
        if filename:
            self.filename = filename

    @property
    def title(self):
        return self._title

    @property
    def menu_id(self):
        return self._menu_id

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._title = ''
        match = RE_TITLE.search(content)
        if match:
            self._title = match.group(1)

        self._menu_id = ''
        match = RE_MENU.search(content)
        if match:
            self._menu_id = match.group(1)

        if RE_MARKDOWN.search(content):
            self._content = markdown(content)
        else:
            self._content = content
