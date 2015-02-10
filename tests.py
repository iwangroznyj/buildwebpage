import unittest
import buildwebpagelib as bw


class Template(unittest.TestCase):

    def test_insert_content(self):
        subpage = bw.Subpage('content')
        tmpl = bw.Template('before <!-- CONTENT --> after')
        self.assertEqual(tmpl.insert_subpage(subpage), 'before content after')


if __name__ == '__main__':
    unittest.main()
