import sys

def warnf(*args, **kwargs):
    print('[Warning]: ', *args, file=sys.stderr, **kwargs)
