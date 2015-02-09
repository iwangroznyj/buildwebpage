import argparse

from glob import iglob
from os import mkdir
from os.path import basename, isdir, join

from .webpage import Subpage, Template
from . import warning


VERSION = '1.2'
# TODO update description
DESCRIPTION = '''Creates a webpage by inserting subpages into a template file.

The template file has to contain the comment `<!-- content -->` which is then
replaced by the content of the subpages.  By default all files starting with an
underscore `_` will be used as subpages.  This can be overridden by naming
subpages manually using either the command-line or the configuration file.

Apart from HTML this script supports input files using Markdown.  A file can be
set to be Markdown by inserting the comment `<!-- markdown -->`.  It will then
automatically converted to HTML when included into the template.

Each subpage can be assigned a title by including the HTML comment
`<!-- title: SOME TITLE TEXT -->`.  The title text given here will be inserted
in place of any occurence of `<!-- title -->` in the template.

Additionally one can mark a specific tag in the template to be the menu item
associated with a subpage by refering to its id using the
`<!-- menu: TAG ID -->` comment.  Any tag that contains the attribute
`id='TAG ID'` will be added a `class='menu-current'` which can then be
formatted using css.

The resulting webpage files will be created in the directory which is set to be
the destination folder.  In process all files will be stripped off the leading
underscore.'''

DEFAULT_TEMPLATE = '_template.html'
DEFAULT_DEST = '.'
DEFAULT_SRCDIR = './_src'


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
                yield Subpage(f.read(), filename)
        except IOError as error:
            warning.warnf('Could not read {}'.format(filename))
            warning.warnf(error)


def create_webpage(templ, subpages, destination):
    if not isdir(destination):
        mkdir(destination)
    for subpage in subpages:
        output_file = join(destination, basename(subpage.filename))
        composed = templ.insert_subpage(subpage)
        print(templ.filename, ' + ', subpage.filename, ' => ', output_file)
        try:
            with open(output_file, 'w') as f:
                f.write(composed)
        except IOError as error:
            warning.warnf(error)
