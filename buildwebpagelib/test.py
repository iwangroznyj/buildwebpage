import unittest
from . import subpage
from . import template


TEMPLATE = u'''<?xml version='1.0' encoding='UTF-8'?>
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN'
'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>
{0}
<p id='test_menuitem'>Menu</p>
{1}
u'ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434'
</html>
'''
TMPL_TITLE = '<head><title><!-- title --></title></head>'
TMPL_CONTENT = '<body><!-- content --></body>'
SUBP_CONTENT = u'ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434'
SUBP_TITLE = '<!-- title: This is a test page! -->'
SUBP_MENUOK = '<!-- menu: test_menuitem -->'
SUBP_MENUBAD = '<!-- menu: test_nonexistent -->'


class TestSubpage(unittest.TestCase):
    def setUp(self):
        self.sub = SUBP_CONTENT
        self.sub_title = SUBP_TITLE + SUBP_CONTENT
        self.sub_menuok = SUBP_MENUOK + SUBP_CONTENT
        self.sub_menubad = SUBP_MENUBAD + SUBP_CONTENT
        self.sub_menutitle = SUBP_TITLE + SUBP_CONTENT + SUBP_MENUOK

    def test_html_subpage(self):
        # create html subpage without title/menu
        test_sub = subpage.HtmlSubpage(self.sub)
        self.assertFalse(test_sub.has_title)
        self.assertFalse(test_sub.has_menu)

        # create html subpage with title
        test_sub = subpage.HtmlSubpage(self.sub_title)
        self.assertTrue(test_sub.has_title)
        self.assertEqual(test_sub.title, 'This is a test page!')
        self.assertFalse(test_sub.has_menu)

        # create html subpage with menu id
        test_sub = subpage.HtmlSubpage(self.sub_menuok)
        self.assertFalse(test_sub.has_title)
        self.assertTrue(test_sub.has_menu)
        self.assertEqual(test_sub.menu, 'test_menuitem')

        # create html subpage with title
        test_sub = subpage.HtmlSubpage(self.sub_menutitle)
        self.assertTrue(test_sub.has_title)
        self.assertEqual(test_sub.title, 'This is a test page!')
        self.assertTrue(test_sub.has_menu)
        self.assertEqual(test_sub.menu, 'test_menuitem')


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.templ_nocont = TEMPLATE.format('', '')
        self.templ = TEMPLATE.format('', TMPL_CONTENT)
        self.templ_title = TEMPLATE.format(TMPL_TITLE, TMPL_CONTENT)

    def test_construct_template(self):
        # template without substitution string is faulty
        with self.assertRaises(template.TemplateNoContentError):
            template.Template(self.templ_nocont)
        # template with substitution string should be alright
        test_template = template.Template(self.templ)
        self.assertFalse(test_template.has_title)
        # title should be recognised within a template
        test_template = template.Template(self.templ_title)
        self.assertTrue(test_template.has_title)


if __name__ == '__main__':
    unittest.main()
