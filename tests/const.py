# template strings
TEMPLATE = u'''<html>
<head><title>\xf6\u044b - {0}</title></head>
<body><p id='test_menuitem'>Menu</p>
{1}
</body></html>
'''
TMPL_TITLE = '<!-- title -->'
TMPL_CONTENT = '<!-- content -->'

# subpage strings
SUBPAGE = u'ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434'
SUB_TITLE = '<!-- title: This is a test page! -->'
SUB_MENUOK = '<!-- menu: test_menuitem -->'
SUB_MENUBAD = '<!-- menu: test_nonexistent -->'

# comparison strings
CMP_BARE = u'''<html>
<head><title>\xf6\u044b - <!-- title --></title></head>
<body><p id='test_menuitem'>Menu</p>
ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434
</body></html>
'''
CMP_TITLE = u'''<html>
<head><title>\xf6\u044b - This is a test page!</title></head>
<body><p id='test_menuitem'>Menu</p>
<!-- title: This is a test page! -->
ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434
</body></html>
'''
CMP_MENU = u'''<html>
<head><title>\xf6\u044b - <!-- title --></title></head>
<body><p id='test_menuitem' class='menu_current' >Menu</p>
<!-- menu: test_menuitem -->
ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434
</body></html>
'''
CMP_MENUBAD = u'''<html>
<head><title>\xf6\u044b - <!-- title --></title></head>
<body><p id='test_menuitem'>Menu</p>
<!-- menu: test_nonexistent -->
ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434
</body></html>
'''
