import re

from markdown import markdown

from .warning import warnf

__all__ = ['Subpage', 'Template']


RE_SUBPAGE_TITLE = re.compile(r'<!--\s*title\s*:\s*(.+?)\s*-->', re.U | re.I)
RE_SUBPAGE_MENUID = re.compile(r'<!--\s*menu_id\s*:\s*(.+?)\s*-->', re.U | re.I)
RE_MARKDOWN = re.compile(r'<!--\s*markdown\s*-->', re.U | re.I)

RE_TEMPL_CONTENT = re.compile(r'<!--\s*CONTENT\s*-->', re.U | re.I)
RE_TEMPL_TITLE = re.compile(r'<!--\s*TITLE\s*-->', re.U | re.I)

# building blocks for regexes matching html attributes (menu_id="xxx")
MENU_ATTR = r'(<.*?MENU_ID\s*=\s*[\'"]{}[\'"])(.*?>)'
MENU_SUBSTITUTION = r"\1 class='menu-current' \2"


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
        match = RE_SUBPAGE_TITLE.search(content)
        if match:
            self._title = match.group(1)

        self._menu_id = ''
        match = RE_SUBPAGE_MENUID.search(content)
        if match:
            self._menu_id = match.group(1)

        if RE_MARKDOWN.search(content):
            self._content = markdown(content)
        else:
            self._content = content


class Template(object):

    def __init__(self, content, filename=None):
        self.filename = ''
        if filename:
            self.filename = filename
        self.content = content
        self.has_title = False
        if not RE_TEMPL_CONTENT.search(content):
            raise ValueError('Template lacks substitution string')
        if RE_TEMPL_TITLE.search(content):
            self.has_title = True

    def insert_subpage(self, subpage):
        whole_page = self.content
        if self.has_title:
            if subpage.title:
                whole_page = RE_TEMPL_TITLE.sub(subpage.title, whole_page)
            else:
                warnf('Missing title in subpage ', subpage.filename)

        if subpage.menu_id:
            pattern = re.compile(MENU_ATTR.format(subpage.menu_id), re.U | re.I)
            if pattern.search(whole_page):
                whole_page = pattern.sub(MENU_SUBSTITUTION, whole_page)
            else:
                warnf('Missing menu item in template: ', subpage.menu_id)

        return RE_TEMPL_CONTENT.sub(subpage.content, whole_page)
