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
