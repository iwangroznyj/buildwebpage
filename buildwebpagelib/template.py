import re

from . import warning

__all__ = ['Template']


RE_TEMPL_CONTENT = re.compile(r'<!--\s*CONTENT\s*-->', re.U | re.I)
RE_TEMPL_TITLE = re.compile(r'<!--\s*TITLE\s*-->', re.U | re.I)

# building blocks for regexes matching html attributes (menu_id="xxx")
MENU_ATTR = r'(<.*?MENU_ID\s*=\s*[\'"]{}[\'"])(.*?>)'
MENU_SUBSTITUTION = r"\1 class='menu-current' \2"


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
                warning.warnf('Missing title in subpage {}'.format(subpage.filename))

        if subpage.menu_id:
            pattern = re.compile(MENU_ATTR.format(subpage.menu_id), re.U | re.I)
            if pattern.search(whole_page):
                whole_page = pattern.sub(MENU_SUBSTITUTION, whole_page)
            else:
                warning.warnf('Missing menu item in template: {}'.format(subpage.menu_id))

        return RE_TEMPL_CONTENT.sub(subpage.content, whole_page)
