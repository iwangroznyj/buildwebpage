import argparse
import ConfigParser
import glob
from . import cfg


# List of properties
PROPERTIES = ['template', 'subpages', 'dest', 'conf']

# Command line help strings
HLP_TEMPL = 'file containing the template for the webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_TEMPLATE)
HLP_SUBPG = 'file containing a subpage of the webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_SUBPAGES)
HLP_CONF = 'configuration file \
(defaults to \'{0}\')'.format(cfg.DEFAULT_CONF)
HLP_DEST = 'destination folder of the finished webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_DEST)


def acquire_settings():
    settings = {'template': cfg.DEFAULT_TEMPLATE,
                'subpages': glob.glob(cfg.DEFAULT_SUBPAGES),
                'dest': cfg.DEFAULT_DEST,
                'conf': cfg.DEFAULT_CONF}
    settings.update(parse_commandline())
    settings.update(parse_configfile(settings['conf']))
    return settings


def parse_commandline():
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('template', nargs='?', help=HLP_TEMPL)
    parser.add_argument('subpages', nargs='*', metavar='subpage',
                        help=HLP_SUBPG)
    parser.add_argument('-c', '--conf', metavar='FILE', help=HLP_CONF)
    parser.add_argument('-d', '--dest', dest='dest', metavar='DIR',
                        help=HLP_DEST)
    return parser.parse_args().__dict__


def parse_configfile(filename):
    # TODO parse data
    config = ConfigParser.SafeConfigParser()
    config.read(filename)
    if not config.has_section(cfg.CONFIG_SECTION):
        return dict()
    return dict((key, var) for key, var in config.items(cfg.CONFIG_SECTION)
                if key in PROPERTIES)
