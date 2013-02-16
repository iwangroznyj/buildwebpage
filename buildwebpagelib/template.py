import re
from . import cfg


REGEX_CONTENT = re.compile(cfg.COMMENT_R.format(cfg.TMPL_CONTENT),
                           re.UNICODE | re.IGNORECASE)
REGEX_TITLE = re.compile(cfg.COMMENT_R.format(cfg.TMPL_TITLE),
                         re.UNICODE | re.IGNORECASE)


class TemplateNoContentError(Exception):
    pass


class Template(object):
    def __init__(self, content):
        self.content = content
        self.has_title = False
        if not REGEX_CONTENT.search(content):
            raise TemplateNoContentError()
        if REGEX_TITLE.search(content):
            self.has_title = True

    def assemble_page(self, subpage):
        raise NotImplementedError  # TODO implement subpages first
