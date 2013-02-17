import sys


WARNING_MESSAGE = '[Warning]: {message}\n'


def warnf(message):
    sys.stderr.write(WARNING_MESSAGE.format(message=message))
