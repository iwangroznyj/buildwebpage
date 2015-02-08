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


def read_template(filename):
    '''Open the template file and create a Template.

    :param filename: name of the template file
    :type  filename: str
    :return:         loaded template
    :rtype:          Template

    '''
    with open(filename, 'r', encoding='utf-8') as fileptr:
        content = fileptr.read()
    return Template(content, filename)


class TemplateContentError(Exception):
    '''Error raised by the Template class if it lacks the content string.'''


class Template(object):
    '''Representation of a webpage template.'''

    def __init__(self, content, filename=None):
        '''Create template.

        :param content: content of the template
        :type  content: str
        :raises TemplateContentError: if the template lacks the string which
                                      should be replaced by the subpage.

        '''
        self.filename = ''
        if filename:
            self.filename = filename
        self.content = content
        self.has_title = False
        if not RE_CONTENT.search(content):
            raise TemplateContentError('Template lacks substitution string')
        if RE_TITLE.search(content):
            self.has_title = True

    def insert_subpage(self, subpage):
        '''Place the subpage into the template.

        :param subpage: subpage to be inserted as content
        :type  subpage: subpage.Subpage
        :return:        built webpage
        :rtype:         str

        '''
        composed_page = self.content
        if self.has_title:
            if subpage.title:
                composed_page = RE_TITLE.sub(subpage.title, composed_page)
            else:
                warning.warnf(WARN_SUBPG_TITLE)
        elif subpage.title:
            warning.warnf(WARN_TEMPL_TITLE)
        if subpage.menu_id:
            re_menu = re.compile(cfg.RE_TEMPL_MENUID.format(subpage.menu_id))
            if re_menu.search(composed_page):
                composed_page = re_menu.sub(MENU_SUBSTITUTION, composed_page)
            else:
                warning.warnf(WARN_TEMPL_MENU)
        return RE_CONTENT.sub(subpage.content, composed_page)
