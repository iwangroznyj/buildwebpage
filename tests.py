import unittest
import buildwebpagelib as bw


class Template(unittest.TestCase):

    def test_insert_content(self):
        subpage = bw.Subpage('content')
        tmpl = bw.Template('before <!-- CONTENT --> after')
        self.assertEqual(tmpl.insert_subpage(subpage), 'before content after')

    def test_insert_title(self):
        subpage = bw.Subpage('<!-- TITLE: le title -->')
        tmpl = bw.Template('before <!-- TITLE --> after')
        self.assertEqual(tmpl.insert_subpage(subpage), 'before le title after')

    def test_insert_menu_item(self):
        subpage = bw.Subpage('<!-- MENU_ID: subpage -->')
        tmpl = bw.Template('before <span id="subpage"> after')
        self.assertEqual(tmpl.insert_subpage(subpage),
                         'before <span id="subpage" class=\'menu-current\' > after')


if __name__ == '__main__':
    unittest.main()
