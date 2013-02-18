#! /usr/bin/env python


import buildwp.cli


def main():
    args = buildwp.cli.parse_commandline()
    print args


if __name__ == '__main__':
    main()
