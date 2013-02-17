# default input and output files
DEFAULT_FILE_PREFIX = '_'
DEFAULT_TEMPLATE = 'template.html'
BUILD_DEST = './build/'

# html comment with and without regex
COMMENT = '<!-- {0} -->'
COMMENT_R = r'<!--\s*{0}\s*-->'
PROPERTY_R = r'{0}\s*:\s*(.+?)'

# menu item regex
MENU_R = '\\<.*?<id=[\'"](\\w+)[\'"].*?\\>'
# current menu item class
MENU_CURRENT = 'class=\'menu_current\''

# template substitution strings
TMPL_CONTENT = 'content'
TMPL_TITLE = 'title'

# subpage strings
SUBP_TITLE = PROPERTY_R.format('title')
SUBP_MENU = PROPERTY_R.format('menu')
