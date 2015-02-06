'''Command-line and config file parsing.

This module contains the Settings class which draws its options from the
command-line and a config file.  The options are overridden in the
following order:

 * the default settings are overridden by settings from the config file
 * config file and default settings are overridden by command-line
    arguments

'''

__all__ = ['get_settings']

import argparse
import glob

from . import cfg


FILEPREFIX = '_'
DEFAULT_TEMPLATE = 'template.html'
DEFAULT_DEST = 'build/'

HLP_TEMPL = 'template for the webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_TEMPLATE)
HLP_SUBPG = 'subpage of the webpage \
(defaults to all files starting with \'{0}\' \
in the current folder)'.format(cfg.FILEPREFIX)
HLP_DEST = 'destination folder of the finished webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_DEST)


def get_settings(args):
    '''Create the dictionary and set options.

    :param args: command-line arguments
    :type  args: list of str
    :return:     application settings
    :rtype:      dict

    '''
    settings = {'template': cfg.DEFAULT_TEMPLATE,
                'dest': cfg.DEFAULT_DEST,
                'conf': cfg.DEFAULT_CONF}
    cli_args = parse_commandline(args)
    if 'conf' in cli_args:
        settings['conf'] = cli_args['conf']
    settings.update(cli_args)
    if 'subpages' not in settings:
        settings['subpages'] = glob.glob(cfg.FILEPREFIX + '*')
    return settings


def parse_commandline(args):
    '''Parse command-line arguments.

    :param args: command-line arguments
    :type  args: list of str
    :return:     settings
    :rtype:      dict

    '''
    parser = argparse.ArgumentParser(
        description=cfg.DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        argument_default=argparse.SUPPRESS)
    parser.add_argument('template', nargs='?', help=HLP_TEMPL)
    parser.add_argument('subpages', nargs='*', metavar='subpage',
                        help=HLP_SUBPG)
    parser.add_argument('-d', '--dest', dest='dest', metavar='DIR',
                        help=HLP_DEST)
    return parser.parse_args(args).__dict__
