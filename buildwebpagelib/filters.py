import re
import markdown


__all__ = ['convert_markdown']

RE_MARKDOWN = re.compile(r'<!--\s*markdown\s*-->', re.U | re.I)


def convert_markdown(string):
    if not RE_MARKDOWN.search(string):
        return string
    return markdown.markdown(string)
