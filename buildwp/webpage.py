'''Classes for representing whole webpages.'''


import os.path
import re

from . import cfg
from . import template
from . import subpage
from . import warning


class WebpageSubpageError(Exception):
    '''Error raised by the Webpage class if there are no subpages given.'''


class Webpage(object):
    '''Representation of a whole webpage with several subpages.'''

    def __init__(self, settings):
        '''Prepare webpage for build process.

        :param settings: settings of buildwebpage
        :type  settings: dict
        :raises WebpageSubpageError: if there are no subpage files given.

        The Webpage expects following `settings`:
         * template: name of the template file
         * subpages: list of the names of the subpage files
         * dest: destination folder where the finished webpage will be located

        '''
        if not settings['subpages']:
            raise WebpageSubpageError('No subpages found')
        self.templatefile = settings['template']
        self.subpagefiles = settings['subpages']
        self.fileprefix = ''
        if len(settings['subpages']) > 1:
            filebases = [os.path.basename(s) for s in settings['subpages']]
            self.fileprefix = os.path.commonprefix(filebases)
        self.dest = settings['dest']
        self.template = self._open_template()
        self.subpages = [subpage.read_subpagefile(filename)
                         for filename in self.subpagefiles]
        self.subpages = [sub for sub in self.subpages if sub]

    def build_webpage(self):
        '''Build the webpage from the template using the subpages.

        The finnished webpage will be placed into the folder specified by
        `self.dest`.

        '''
        templatefile = os.path.basename(self.templatefile)
        if not os.path.isdir(self.dest):
            os.makedirs(self.dest)
        for page in self.subpages:
            oldfile = os.path.basename(page.filename)
            newfile = oldfile[len(self.fileprefix):]
            newfile = os.path.join(self.dest, newfile)
            print '{0} + {1} => {2}'.format(templatefile, oldfile, newfile)
            finalpage = self.template.build_page(page)
            try:
                with open(newfile, 'w') as fileptr:
                    fileptr.write(finalpage.encode(cfg.INPUTENC))
            except IOError as error:
                warning.warnf(str(error))

    def _open_template(self):
        '''Open the template file and create Template object

        :return: loaded template
        :rtype:  template.Template

        '''
        with open(self.templatefile) as fileptr:
            content = unicode(fileptr.read(), cfg.INPUTENC)
        return template.Template(content)
