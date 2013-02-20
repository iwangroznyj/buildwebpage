'''Classes representing the template for the webpage.'''


import re
from . import cfg
from . import warning


# Precompile regexes
RE_CONTENT = re.compile(cfg.RE_TEMPL_CONTENT, re.UNICODE | re.IGNORECASE)
RE_TITLE = re.compile(cfg.RE_TEMPL_TITLE, re.UNICODE | re.IGNORECASE)
MENU_SUBSTITUTION = r"\1 class='{0}' \2".format(cfg.SUBST_CURRENTMENU)

# Warning messages
WARN_SUBPG_TITLE = 'Subpage does not set title for template\'s title slot'
WARN_TEMPL_TITLE = 'Template lacks title slot for title set by subpage'
WARN_TEMPL_MENU = 'Template lacks menu item referenced by subpage'
ERR_TEMPL_CONTENT = 'Template lacks content string'


class TemplateContentError(Exception):
    '''Error raised by the Template class if it lacks the content string.'''


class Template(object):
    '''Representation of a webpage template.'''

    def __init__(self, content):
        '''Create template.

        :param content: content of the template
        :type  content: unicode
        :raises TemplateContentError: if the template lacks the string which
                                      should be replaced by the subpage.

        '''
        self.content = content
        self.has_title = False
        if not RE_CONTENT.search(content):
            raise TemplateContentError('Template lacks substitution string')
        if RE_TITLE.search(content):
            self.has_title = True

    def build_page(self, subpage):
        '''Place the subpage into the template.

        :param subpage: subpage to be inserted as content
        :type  subpage: subpage.Subpage
        :return:        built webpage
        :rtype:         unicode

        '''
        webpage = self.content
        if self.has_title:
            if subpage.has_title:
                webpage = RE_TITLE.sub(subpage.title, webpage)
            else:
                warning.warnf(WARN_SUBPG_TITLE)
        elif webpage.has_title:
            warning.warnf(WARN_TEMPL_TITLE)
        if subpage.has_menu:
            re_menu = re.compile(cfg.RE_TEMPL_MENUID.format(subpage.menu))
            if re_menu.search(webpage):
                webpage = re_menu.sub(MENU_SUBSTITUTION, webpage)
            else:
                warning.warnf(WARN_TEMPL_MENU)
        return RE_CONTENT.sub(subpage.get_html(), webpage)
