'''Tests for the buildwp.subpage module'''


import unittest
import buildwebpagelib as bw
from . import const


class TestSubpage(unittest.TestCase):
    '''Test the subpage class'''

    def setUp(self):
        '''Set up the test environment.'''
        self.sub = const.SUBPAGE
        self.sub_title = const.SUB_TITLE + const.SUBPAGE
        self.sub_menuok = const.SUB_MENUOK + const.SUBPAGE
        self.sub_menubad = const.SUB_MENUBAD + const.SUBPAGE
        self.sub_menutitle = const.SUB_TITLE + const.SUBPAGE + const.SUB_MENUOK

    def test_html_subpage(self):
        '''Test if menu/title strings are recognised in html subpages'''
        # create html subpage without title/menu
        test_sub = bw.Subpage(self.sub)
        self.assertFalse(test_sub.has_title)
        self.assertFalse(test_sub.has_menu)

        # create html subpage with title
        test_sub = bw.Subpage(self.sub_title)
        self.assertTrue(test_sub.has_title)
        self.assertEqual(test_sub.title, 'This is a test page!')
        self.assertFalse(test_sub.has_menu)

        # create html subpage with menu
        test_sub = bw.Subpage(self.sub_menuok)
        self.assertFalse(test_sub.has_title)
        self.assertTrue(test_sub.has_menu)
        self.assertEqual(test_sub.menu, 'test_menuitem')

        # create html subpage with title and menu
        test_sub = bw.Subpage(self.sub_menutitle)
        self.assertTrue(test_sub.has_title)
        self.assertEqual(test_sub.title, 'This is a test page!')
        self.assertTrue(test_sub.has_menu)
        self.assertEqual(test_sub.menu, 'test_menuitem')

    def test_markdown_subpage(self):
        '''Test if menu/title strings are recognised in a markdown subpage'''
        mdsub = bw.Subpage(const.SUB_TITLE + '\n' +
                                        const.SUB_MARKDOWN)
        self.assertTrue(mdsub.has_title)
        self.assertEqual(mdsub.title, 'This is a test page!')
        self.assertFalse(mdsub.has_menu)


if __name__ == '__main__':
    unittest.main()
