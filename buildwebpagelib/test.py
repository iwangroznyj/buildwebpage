import unittest
from . import subpage
from . import template


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


class TestSubpage(unittest.TestCase):
    def setUp(self):
        self.sub = SUBPAGE
        self.sub_title = SUB_TITLE + SUBPAGE
        self.sub_menuok = SUB_MENUOK + SUBPAGE
        self.sub_menubad = SUB_MENUBAD + SUBPAGE
        self.sub_menutitle = SUB_TITLE + SUBPAGE + SUB_MENUOK

    def test_html_subpage(self):
        # create html subpage without title/menu
        test_sub = subpage.Subpage(self.sub)
        self.assertFalse(test_sub.has_title)
        self.assertFalse(test_sub.has_menu)

        # create html subpage with title
        test_sub = subpage.Subpage(self.sub_title)
        self.assertTrue(test_sub.has_title)
        self.assertEqual(test_sub.title, 'This is a test page!')
        self.assertFalse(test_sub.has_menu)

        # create html subpage with menu
        test_sub = subpage.Subpage(self.sub_menuok)
        self.assertFalse(test_sub.has_title)
        self.assertTrue(test_sub.has_menu)
        self.assertEqual(test_sub.menu, 'test_menuitem')

        # create html subpage with title and menu
        test_sub = subpage.Subpage(self.sub_menutitle)
        self.assertTrue(test_sub.has_title)
        self.assertEqual(test_sub.title, 'This is a test page!')
        self.assertTrue(test_sub.has_menu)
        self.assertEqual(test_sub.menu, 'test_menuitem')


class TestTemplate(unittest.TestCase):
    def setUp(self):
        # set templates
        self.templ_nocont = TEMPLATE.format('', '')
        self.templ = TEMPLATE.format('', TMPL_CONTENT)
        self.templ_title = TEMPLATE.format(TMPL_TITLE, TMPL_CONTENT)

        # set subpages
        self.sub = subpage.Subpage(SUBPAGE)
        self.sub_menuok = subpage.Subpage(SUB_MENUOK + '\n' + SUBPAGE)
        self.sub_title = subpage.Subpage(SUB_TITLE + '\n' + SUBPAGE)

    def test_construct_template(self):
        # template without substitution string is faulty
        with self.assertRaises(template.TemplateContentError):
            template.Template(self.templ_nocont)

        # template with substitution string should be alright
        test_template = template.Template(self.templ)
        self.assertFalse(test_template.has_title)

        # title should be recognised within a template
        test_template = template.Template(self.templ_title)
        self.assertTrue(test_template.has_title)

    def test_build_pages(self):
        test_t = template.Template(self.templ_title)
        # no title or menu
        webpage = test_t.build_page(self.sub)
        self.assertEqual(webpage, CMP_BARE)
        # substitute title
        webpage = test_t.build_page(self.sub_title)
        self.assertEqual(webpage, CMP_TITLE)
        # set current menu item
        webpage = test_t.build_page(self.sub_menuok)
        self.assertEqual(webpage, CMP_MENU)
        # ignore menu item mismatch
        webpage = test_t.build_page(self.sub_menubad)
        self.assertEqual(webpage, CMP_MENUBAD)


if __name__ == '__main__':
    unittest.main()
