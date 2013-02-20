#! /usr/bin/env python


import sys

import buildwp.cli
import buildwp.webpage


def main(args):
    settings = buildwp.cli.Settings(args[1:])
    webpage = buildwp.webpage.Webpage(settings)
    webpage.build_webpage()


if __name__ == '__main__':
    main(sys.argv)
