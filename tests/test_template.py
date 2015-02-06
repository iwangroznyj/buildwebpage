'''Tests for the bw.'''


import unittest
import buildwebpagelib as bw
from . import const


class TestTemplate(unittest.TestCase):
    '''Tests for the Template class.'''

    def setUp(self):
        '''Set testing environment.

        All subpages are already initialised as bw.Subpage
        objects.

        '''
        # set templates
        self.templ_nocont = const.TEMPLATE.format('', '')
        self.templ = const.TEMPLATE.format('', const.TMPL_CONTENT)
        self.templ_title = const.TEMPLATE.format(const.TMPL_TITLE,
                                                 const.TMPL_CONTENT)

        # set subpages
        self.sub = bw.Subpage(const.SUBPAGE)
        self.sub_title = bw.Subpage(const.SUB_TITLE + '\n' + const.SUBPAGE)
        self.sub_menuok = bw.Subpage(const.SUB_MENUOK + '\n' + const.SUBPAGE)
        self.sub_menubad = bw.Subpage(const.SUB_MENUBAD + '\n' + const.SUBPAGE)
        self.sub_md = bw.Subpage(const.SUB_TITLE + '\n' + const.SUB_MARKDOWN)

    def test_construct_template(self):
        '''Test the error handling and title recognision of the template.'''
        # template without substitution string is faulty
        with self.assertRaises(bw.TemplateContentError):
            bw.Template(self.templ_nocont)

        # template with substitution string should be alright
        test_template = bw.Template(self.templ)
        self.assertFalse(test_template.has_title)

        # title should be recognised within a template
        test_template = bw.Template(self.templ_title)
        self.assertTrue(test_template.has_title)

    def test_build_pages(self):
        '''Test if the subpages are inserted properly into the template'''
        test_t = bw.Template(self.templ_title)
        # no title or menu
        webpage = test_t.build_page(self.sub)
        self.assertEqual(webpage, const.CMP_BARE)
        # substitute title
        webpage = test_t.build_page(self.sub_title)
        self.assertEqual(webpage, const.CMP_TITLE)
        # set current menu item
        webpage = test_t.build_page(self.sub_menuok)
        self.assertEqual(webpage, const.CMP_MENU)
        # ignore menu item mismatch
        webpage = test_t.build_page(self.sub_menubad)
        self.assertEqual(webpage, const.CMP_MENUBAD)
        # test markdown conversion
        webpage = test_t.build_page(self.sub_md)
        self.assertEqual(webpage, const.CMP_MARKDOWN)


if __name__ == '__main__':
    unittest.main()
