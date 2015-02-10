import unittest
import buildwebpagelib as bw


class Template(unittest.TestCase):

    def test_insert_content(self):
        subpage = bw.Subpage('content')
        tmpl = bw.Template('before <!-- CONTENT --> after')
        self.assertEqual(tmpl.insert_subpage(subpage), 'before content after')

    def test_instert_title(self):
        subpage = bw.Subpage('<!-- TITLE: le title -->')
        tmpl = bw.Template('before <!-- TITLe --> after')
        self.assertEqual(tmpl.insert_subpage(subpage), 'before le title after')


if __name__ == '__main__':
    unittest.main()
