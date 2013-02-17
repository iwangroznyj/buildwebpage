import re
from . import cfg
from . import warning


REGEX_CONTENT = re.compile(cfg.COMMENT_R.format(cfg.TMPL_CONTENT),
                           re.UNICODE | re.IGNORECASE)
REGEX_TITLE = re.compile(cfg.COMMENT_R.format(cfg.TMPL_TITLE),
                         re.UNICODE | re.IGNORECASE)
REGEX_MENU = re.compile(cfg.MENU_R, re.UNICODE | re.IGNORECASE)

WARN_SUB_TITLE = 'Subpage does not set title for template\'s title slot'
WARN_TMP_TITLE = 'Template lacks title slot for title set by subpage'
WARN_TMP_MENU = 'Template lacks menu item referenced by subpage'


class TemplateContentError(Exception):
    pass


class Template(object):
    def __init__(self, content):
        self.content = content
        self.has_title = False
        if not REGEX_CONTENT.search(content):
            raise TemplateContentError()
        if REGEX_TITLE.search(content):
            self.has_title = True

    def build_page(self, subpage):
        webpage = self.content
        if self.has_title:
            if subpage.has_title:
                webpage = REGEX_TITLE.sub(subpage.title, webpage)
            else:
                warning.warnf(WARN_SUB_TITLE)
        elif webpage.has_title:
            warning.warnf(WARN_TMP_TITLE)
        # TODO substitute menu string
        return REGEX_CONTENT.sub(subpage.get_html(), webpage)
