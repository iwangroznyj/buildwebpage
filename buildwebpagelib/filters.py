import re
import markdown


__all__ = ['convert_markdown', 'strip_html_comments']

RE_MARKDOWN = re.compile(r'<!--\s*markdown\s*-->', re.U | re.I)
RE_HTML_COMMENT = re.compile(r'<--.*?-->', re.U)


def convert_markdown(string):
    if not RE_MARKDOWN.search(string):
        return string
    return markdown.markdown(string)


def strip_html_comments(string):
    return RE_HTML_COMMENT.sub('', string)
