'''Programme-wide settings for buildwebpage.

This module contains settings for the buildwebpage script which are not
meant to be edited by the programme user.

'''


# Programme description
DESCRIPTION = '''Creates a webpage by inserting subpages into a template file.

The template file has to contain the comment `<!-- content -->` which is
then replaced by the content of the subpages.  By default all files
starting with an underscore `_` will be used as subpages.  This can be
overridden by naming subpages manually using either the command-line or
the configuration file.

Apart from HTML this script supports input files using Markdown.  A file
can be set to be Markdown by inserting the comment `<!-- markdown -->`.
It will then automatically converted to HTML when included into the
template.

Each subpage can be assigned a title by including the HTML comment
`<!-- title: SOME TITLE TEXT -->`.  The title text given here will be
inserted in place of any occurence of `<!-- title -->` in the template.

Additionally one can mark a specific tag in the template to be the menu
item associated with a subpage by refering to its id using the
`<!-- menu: TAG ID -->` comment.  Any tag that contains the attribute
`id='TAG ID'` will be added a `class='menu_current'` which can then be
formatted using css.

The resulting webpage files will be created in the directory which is
set to be the destination folder.'''

# Default input and output files
DEFAULT_SUBPAGES = '_*'
DEFAULT_TEMPLATE = 'template.html'
DEFAULT_DEST = 'build/'
DEFAULT_CONF = 'buildwebpage.cfg'
DEFAULT_HTMLFORMAT = 'xhtml1'

# Substitution settings
SUBST_CONTENT = 'content'
SUBST_TITLE = 'title'
SUBST_MENU = 'menu'
SUBST_MARKDOWN = 'markdown'
SUBST_ATTRIBUTE = 'id'
SUBST_CURRENTMENU = 'menu_current'

# Encoding of all input files
INPUTENC = 'utf8'

# Html templates
HTML_COMMENT = '<!-- {0} -->'

# Name of the main section in the config file
SECTION_CONFIG = 'settings'
SECTION_SUBPG = 'subpages'

# Partial regexes
_RE_COMMENT = r'<!--\s*{0}\s*-->'
_RE_SUBST_PROPERTY = r'{0}\s*:\s*(.+?)'
_RE_ATTRIBUTE = '(<.*?{0}\s*=\s*[\'"]{1}[\'"])(.*?>)'

# Regexes
RE_TEMPL_TITLE = _RE_COMMENT.format(SUBST_TITLE)
RE_TEMPL_CONTENT = _RE_COMMENT.format(SUBST_CONTENT)
# We don't know what the menuid will be, so the regex gets a replacement field
RE_TEMPL_MENUID = _RE_ATTRIBUTE.format(SUBST_ATTRIBUTE, '{0}')
RE_SUBPG_TITLE = _RE_COMMENT.format(_RE_SUBST_PROPERTY.format(SUBST_TITLE))
RE_SUBPG_MENU = _RE_COMMENT.format(_RE_SUBST_PROPERTY.format(SUBST_MENU))
RE_MARKDOWN = _RE_COMMENT.format(SUBST_MARKDOWN)
