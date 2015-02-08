import argparse
from . import cfg


DEFAULT_TEMPLATE = '_template.html'
DEFAULT_DEST = '.'
DEFAULT_SRCDIR = './_src'


def parse_commandline(args):
    parser = argparse.ArgumentParser(
        description=cfg.DESCRIPTION,
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
