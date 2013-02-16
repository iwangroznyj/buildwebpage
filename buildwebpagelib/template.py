import re
import buildwebpagelib.cfg as cfg


REGEX_CONTENT = re.compile(cfg.COMMENT_R.format(cfg.TMPL_CONTENT),
                           re.UNICODE | re.IGNORECASE)
REGEX_TITLE = re.compile(cfg.COMMENT_R.format(cfg.TMPL_TITLE),
                         re.UNICODE | re.IGNORECASE)

ERR_NOSTR = 'template lacks substitution string \'{string}\'.'


class TemplateError(Exception):


class Template(object):
    def __init__(self, content):
        self.content = content
        self.has_title = False
        if not REGEX_CONTENT.search(content):
            raise TemplateError()  # TODO add sane error message
        if REGEX_TITLE.search(content):
            self.has_title = True

    def assemble_page(self, subpage):
        raise NotImplementedError  # TODO implement subpages first
