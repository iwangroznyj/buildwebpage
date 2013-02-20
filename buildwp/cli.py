'''Command-line and config file parsing.

This module contains the Settings class which draws its options from the
command-line and a config file.  The options are overridden in the
following order:

 * the default settings are overridden by settings from the config file
 * config file and default settings are overridden by command-line
    arguments

'''


import argparse
import ConfigParser
import glob

from . import cfg


# Default values
DEFAULTS = {'template': cfg.DEFAULT_TEMPLATE,
            'subpages': glob.glob(cfg.DEFAULT_SUBPAGES),
            'dest': cfg.DEFAULT_DEST,
            'conf': cfg.DEFAULT_CONF}

# Command line help strings
SUBSTSTRING = cfg.HTML_COMMENT.format(cfg.SUBST_CONTENT)
# TODO rewrite description (talk about prefixes, menuids, title etc)
DESC = '''Creates a webpage by inserting subpages into a template file.  The
template file has to contain the string '{subststring}' which is then replaced
by the content of the subpages.  The resulting webpage files will be created in
the folder specified as 'destination folder'.
'''.format(subststring=SUBSTSTRING)
HLP_TEMPL = 'template for the webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_TEMPLATE)
HLP_SUBPG = 'subpage of the webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_SUBPAGES)
HLP_CONF = 'configuration file \
(defaults to \'{0}\')'.format(cfg.DEFAULT_CONF)
HLP_DEST = 'destination folder of the finished webpage \
(defaults to \'{0}\')'.format(cfg.DEFAULT_DEST)
HLP_GENCFG = 'save current configuration to the file specified by the \
-c/--config argument'

# Config file builder
CFG_SECTION = '[{section}]\n{options}'
CFG_OPTION = '{option} = {value}'


class Settings(dict):
    '''Settings dictionary.

    This class is a dictionary (i.e. a subclass of dict) which draws its
    content from both the command-line and the config file.

    '''

    def __init__(self, args):
        '''Create the dictionary and set options.

        :param args: command-line arguments
        :type  args: list of str

        '''
        super(Settings, self).__init__(DEFAULTS)
        cli_args = self.parse_commandline(args)
        if 'conf' in cli_args:
            self['conf'] = cli_args['conf']
        cfg_args = self.parse_configfile(self['conf'])
        self.update(cfg_args)
        self.update(cli_args)
        if 'gencfg' in cli_args:
            self.write_configfile(self['conf'])

    def parse_commandline(self, args):
        '''Parse command-line arguments.

        :param args: command-line arguments
        :type  args: list of str
        :return:     settings
        :rtype:      dict

        '''
        parser = argparse.ArgumentParser(description=DESC,
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

    def parse_configfile(self, filename):
        '''Parse settings in the config file.

        :param filename: name of the config file
        :type  filename: str
        :return:         settings
        :rtype:          dict

        '''
        config = ConfigParser.SafeConfigParser(allow_no_value=True)
        config.read(filename)
        content = dict()
        if config.has_section(cfg.SECTION_CONFIG):
            content.update((key, var)
                           for key, var in config.items(cfg.SECTION_CONFIG)
                           if key in DEFAULTS.keys())
        if config.has_section(cfg.SECTION_SUBPG):
            content['subpages'] = config.options(cfg.SECTION_SUBPG)
        return content

    def write_configfile(self, filename):
        '''Write current settings to a config file.

        :param filename: name of the config file
        :type  filename: str

        '''
        options = [CFG_OPTION.format(option=option, value=value)
                   for option, value in self.items()
                   if option in ['template', 'dest']]
        settings = CFG_SECTION.format(section=cfg.SECTION_CONFIG,
                                      options='\n'.join(options))
        subpages = CFG_SECTION.format(section=cfg.SECTION_SUBPG,
                                      options='\n'.join(self['subpages']))
        config = settings + '\n\n' + subpages
        with open(filename, 'w') as cfgfile:
            cfgfile.write(config)
