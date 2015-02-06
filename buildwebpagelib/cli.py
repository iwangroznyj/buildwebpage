'''Command-line and config file parsing.

This module contains the Settings class which draws its options from the
command-line and a config file.  The options are overridden in the
following order:

 * the default settings are overridden by settings from the config file
 * config file and default settings are overridden by command-line
    arguments

'''


import argparse
import configparser
import glob

from . import cfg


# Command line help strings
HLP_TEMPL = 'template for the webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_TEMPLATE)
HLP_SUBPG = 'subpage of the webpage \
(defaults to all files starting with \'{0}\' \
in the current folder)'.format(cfg.FILEPREFIX)
HLP_CONF = 'configuration file \
(defaults to \'{0}\')'.format(cfg.DEFAULT_CONF)
HLP_DEST = 'destination folder of the finished webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_DEST)
HLP_GENCFG = 'save current configuration to the file specified by the \
-c/--config argument'
# Config file builder
CFG_SECTION = '[{section}]\n{options}'
CFG_OPTION = '{option} = {value}'


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
    cfg_args = parse_configfile(settings['conf'])
    settings.update(cfg_args)
    settings.update(cli_args)
    if not 'subpages' in settings:
        settings['subpages'] = glob.glob(cfg.FILEPREFIX + '*')
    if 'gencfg' in cli_args:
        write_configfile(settings, settings['conf'])
    return settings


def parse_commandline(args):
    '''Parse command-line arguments.

    :param args: command-line arguments
    :type  args: list of str
    :return:     settings
    :rtype:      dict

    '''
    parser = argparse.ArgumentParser(description=cfg.DESCRIPTION,
                                     formatter_class=
                                     argparse.RawDescriptionHelpFormatter,
                                     argument_default=argparse.SUPPRESS)
    parser.add_argument('template', nargs='?', help=HLP_TEMPL)
    parser.add_argument('subpages', nargs='*', metavar='subpage',
                        help=HLP_SUBPG)
    parser.add_argument('-c', '--conf', metavar='FILE', help=HLP_CONF)
    parser.add_argument('-d', '--dest', dest='dest', metavar='DIR',
                        help=HLP_DEST)
    parser.add_argument('--gen-config', dest='gencfg', action='store_true',
                        help=HLP_GENCFG)
    return parser.parse_args(args).__dict__


def parse_configfile(filename):
    '''Parse settings in the config file.

    :param filename: name of the config file
    :type  filename: str
    :return:         settings
    :rtype:          dict

    '''
    config = configparser.SafeConfigParser(allow_no_value=True)
    config.read(filename)
    content = dict()
    if config.has_section(cfg.SECTION_CONFIG):
        content.update((key, var)
                       for key, var in config.items(cfg.SECTION_CONFIG)
                       if key in ['template', 'dest'])
    if config.has_section(cfg.SECTION_SUBPG):
        content['subpages'] = config.options(cfg.SECTION_SUBPG)
    return content


def write_configfile(settings, filename):
    '''Write current settings to a config file.

    :param filename: name of the config file
    :type  filename: str

    '''
    options = [CFG_OPTION.format(option=option, value=value)
               for option, value in list(settings.items())
               if option in ['template', 'dest']]
    sec_settings = CFG_SECTION.format(section=cfg.SECTION_CONFIG,
                                      options='\n'.join(options))
    sec_subpages = CFG_SECTION.format(section=cfg.SECTION_SUBPG,
                                      options='\n'.join(settings['subpages']))
    config = sec_settings + '\n\n' + sec_subpages
    with open(filename, 'w', encoding=cfg.INPUTENC) as cfgfile:
        cfgfile.write(config)
