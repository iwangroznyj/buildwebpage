#! /usr/bin/env python3

from distutils.core import setup
import buildwebpagelib as bw


# TODO url, download_url
config = {'name': 'buildwebpage',
          'version': bw.VERSION,
          'author': 'Johannes Englisch',
          'author_email': 'cyberjoe0815@hotmail.com',
          'description': 'Build static webpages using a template',
          'long_description': bw.DESCRIPTION,
          'classifiers': ['Development Status :: 4 - Beta',
                          'Environment :: Console',
                          'Intended Audience :: Developers',
                          'License :: OSI Approved :: MIT License',
                          'Operating System :: OS Independent',
                          'Programming Language :: Python :: 3',
                          'Topic :: Internet :: WWW/HTTP :: Site Management'],
          'requires': ['Markdown'],
          'packages': ['buildwebpagelib'],
          'scripts': ['buildwebpage']}

setup(**config)
