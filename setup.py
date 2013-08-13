#! /usr/bin/env python

'''Buildwebpage setup script.

Uses distutils in order to install the buildwebpage script or create
distributable packages.

'''


from distutils.core import setup
import buildwp.cfg


# TODO url, download_url
config = {'name': 'buildwebpage',
          'version': buildwp.cfg.VERSION,
          'author': 'Johannes Englisch',
          'author_email': 'cyberjoe0815@hotmail.com',
          'description': 'Build static webpages using a template',
          'long_description': buildwp.cfg.DESCRIPTION,
          'classifiers': ['Development Status :: 4 - Beta',
                          'Environment :: Console',
                          'Intended Audience :: Developers',
                          'License :: OSI Approved :: MIT License',
                          'Operating System :: OS Independent',
                          'Programming Language :: Python :: 3',
                          'Topic :: Internet :: WWW/HTTP :: Site Management'],
          'requires': ['Markdown'],
          'packages': ['buildwp'],
          'scripts': ['buildwebpage']}

setup(**config)
