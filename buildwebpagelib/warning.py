'''Very basic system for printing warning messages on the screen.'''


import sys


WARNING_MESSAGE = '[Warning]: {message}\n'


def warnf(message):
    '''Print warning message to stderr.

    :param message: message to be printed
    :type  message: str

    '''
    sys.stderr.write(WARNING_MESSAGE.format(message=message))
