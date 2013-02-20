import os.path
import re

from . import cfg
from . import template
from . import subpage
from . import warning


# Markdown regex
RE_MARKDOWN = re.compile(cfg.RE_MARKDOWN, re.UNICODE | re.IGNORECASE)


class WebpageNoSubpageError(Exception):
    pass


class Webpage(object):
    def __init__(self, settings):
        if not settings['subpages']:
            raise WebpageNoSubpageError('no subpages found')
        self.templatefile = settings['template']
        self.subpagefiles = settings['subpages']
        self.fileprefix = ''
        if len(settings['subpages']) > 1:
            filebases = [os.path.basename(s) for s in settings['subpages']]
            self.fileprefix = os.path.commonprefix(filebases)
        self.dest = settings['dest']
        self.template = self._open_template()
        self.subpages = self._open_subpages()

    def build_webpage(self):
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

    def _open_subpages(self):
        subpages = list()
        for filename in self.subpagefiles:
            try:
                with open(filename) as fileptr:
                    content = unicode(fileptr.read(), cfg.INPUTENC)
            except IOError as error:
                warning.warnf(str(error))
                continue
            if RE_MARKDOWN.search(content):
                sub = subpage.MarkdownSubpage(content, filename)
            else:
                sub = subpage.Subpage(content, filename)
            subpages.append(sub)
        return subpages

    def _open_template(self):
        with open(self.templatefile) as fileptr:
            content = unicode(fileptr.read(), cfg.INPUTENC)
        return template.Template(content)
