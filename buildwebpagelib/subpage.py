from . import cfg


REGEX_TITLE = re.compile(cfg.COMMENT_R.format(cfg.SUBP_TITLE),
                         re.UNICODE | re.IGNORECASE)
REGEX_MENU = re.compile(cfg.COMMENT_R.format(cfg.SUBP_MENU),
                        re.UNICODE | re.IGNORECASE)


class SubPageError(Exception):
    pass


class SubPage(object):
    def __init__(self, content, filename):
        self.content = content
        self.has_title = False
        self.title = ''
        self.has_menu_id = False
        self.menu_id = ''
        match = REGEX_TITLE.search(content)
        if match:
            self.title = match.group(1)
            self.has_title = True
        match = REGEX_MENU.search(content)
        if match:
            self.menu = match.group(1)
            self.has_menu = True

    def get_html(self):
        raise NotImplementedError


class HtmlSubPage(SubPage):
    def get_html(self):
        return self.content


class MarkdownSubPage(SubPage):
    def get_html(self):
        raise NotImplementedError  # TODO use markdown parser for converting
