import os.path
import sys


WARNING_MESSAGE = '[Warning]: {filename}{message}\n'


class SoftWarning(object):
    def __init__(self, message, filename=None, stream=None):
        self.message = message
        self.filename = filename
        if stream:
            self.stream = stream
        else:
            self.stream = sys.stderr

    def warn(self):
        filestring = ''
        if self.filename:
            filestring = os.path.basename(self.filename) + ': '
        self.stream.write(WARNING_MESSAGE.format(filename=filestring,
                                                 message=self.message))


class SoftWarningNoFile(SoftWarning):
    def __init__(self, message):
        super(SoftWarningNoFile, self).__init__(message, filename=None)
