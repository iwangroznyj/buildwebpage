import argparse

from glob import iglob
from os import mkdir
from os.path import basename, isdir, join

from .webpage import Subpage, Template
from .warning import warnf
from .filters import convert_markdown, strip_html_comments


DEFAULT_TEMPLATE = '_template.html'
DEFAULT_DEST = '.'
DEFAULT_SRCDIR = './_src'


VERSION = '2.0'
DESCRIPTION = """Creates a webpage by inserting subpages into a template file.

By default the programme looks into the source folder, identifies the template
by its file name and attempts to insert all remaining files in the folder into
the template.

The whole content of a given subpage will be inserted into the template in place
of a `<!-- content -->` comment.  The content itself can be written in html or
in markdown.  For markdown conversion, add a `<!-- markdown -->` comment to
the subpage.

It is also possible to assign a title to a subpage.  A subpage may contain a
comment `<!-- title: SOME TITLE TEXT -->` which will be inserted in place of a
`<!-- title -->` comment in the template.

If the template contains a comment <!-- modified_date -->, the comment will be
replaced with the date the subpage file was last modified.

Additionally one can mark a specific tag in the template to be the menu item
associated with a subpage by refering to its id using the
`<!-- menu: TAG ID -->` comment.  Any tag that contains the attribute
`id='TAG ID'` will be added a `class='menu-current'` which can then be
formatted using css."""


def parse_commandline(args):
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'folder', nargs='?', default=DEFAULT_SRCDIR,
        help='source folder (default: ./_src/)')
    parser.add_argument(
        '-d', '--dest', dest='dest', metavar='DIR', default=DEFAULT_DEST,
        help='destination folder (default: ./)')
    parser.add_argument(
        '-t', '--template', dest='template', metavar='FILE',
        default=DEFAULT_TEMPLATE,
        help='basename of the template file (default: _template.html)')
    return parser.parse_args(args)


def read_template(filename):
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    return Template(content, filename)


def read_subpages(folder, blacklist=()):
    for filename in iglob(join(folder, '*')):
        if basename(filename) in blacklist:
            continue
        try:
            with open(filename, encoding='utf-8') as f:
                yield Subpage(convert_markdown(f.read()), filename)
        except IOError as error:
            warnf('Could not read ', filename)
            warnf(error)


def create_webpage(templ, subpages, destination):
    if not isdir(destination):
        mkdir(destination)
    for subpage in subpages:
        output_file = join(destination, basename(subpage.filename))
        composed = templ.insert_subpage(subpage)
        print(templ.filename, ' + ', subpage.filename, ' => ', output_file)
        try:
            with open(output_file, 'w') as f:
                f.write(strip_html_comments(composed))
        except IOError as error:
            warnf(error)
