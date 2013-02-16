import unittest
from . import template


TEST_TEMPLATE = u'''<?xml version='1.0' encoding='UTF-8'?>
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN'
'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>
{0}
{1}
u'ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434'
</html>
'''
TEST_TMPL_TITLE = '<head><title><!-- title --></title></head>'
TEST_TMPL_CONTENT = '<body><!-- content --></body>'
TEST_SUBP_CONTENT = u'ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434'


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.templ_nocont = TEST_TEMPLATE.format('', '')
        self.templ = TEST_TEMPLATE.format('', TEST_TMPL_CONTENT)
        self.templ_title = TEST_TEMPLATE.format(TEST_TMPL_TITLE,
                                                TEST_TMPL_CONTENT)

    def test_construct_template(self):
        # template without substitution string is faulty
        with self.assertRaises(template.TemplateError):
            template.Template(self.templ_nocont)
        # template with substitution string should be alright
        test_template = template.Template(self.templ)
        self.assertFalse(test_template.has_title)
        # title should be recognised within a template
        test_template = template.Template(self.templ_title)
        self.assertTrue(test_template.has_title)


if __name__ == '__main__':
    unittest.main()
