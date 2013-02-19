#! /usr/bin/env python


import buildwp.cli
import buildwp.webpage


def main():
    settings = buildwp.cli.acquire_settings()
    webpage = buildwp.webpage.Webpage(settings)
    webpage.build_webpage()


if __name__ == '__main__':
    main()
