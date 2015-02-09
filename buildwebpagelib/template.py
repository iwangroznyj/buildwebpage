import re

from . import cfg
from . import warning

__all__ = ['read_template', 'Template']


RE_CONTENT = re.compile(cfg.RE_TEMPL_CONTENT, re.UNICODE | re.IGNORECASE)
RE_TITLE = re.compile(cfg.RE_TEMPL_TITLE, re.UNICODE | re.IGNORECASE)
MENU_SUBSTITUTION = r"\1 class='{0}' \2".format(cfg.SUBST_CURRENTMENU)


def read_template(filename):
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    return Template(content, filename)


class Template(object):

    def __init__(self, content, filename=None):
        self.filename = ''
        if filename:
            self.filename = filename
        self.content = content
        self.has_title = False
        if not RE_CONTENT.search(content):
            raise ValueError('Template lacks substitution string')
        if RE_TITLE.search(content):
            self.has_title = True

    def insert_subpage(self, subpage):
        composed_page = self.content
        if self.has_title:
            if subpage.title:
                composed_page = RE_TITLE.sub(subpage.title, composed_page)
            else:
                warning.warnf('Missing title in subpage {}'.format(subpage.filename))
        if subpage.menu_id:
            re_menu = re.compile(cfg.RE_TEMPL_MENUID.format(subpage.menu_id))
            if re_menu.search(composed_page):
                composed_page = re_menu.sub(MENU_SUBSTITUTION, composed_page)
            else:
                warning.warnf('Missing menu item in template: {}'.format(subpage.menu_id))
        return RE_CONTENT.sub(subpage.content, composed_page)
