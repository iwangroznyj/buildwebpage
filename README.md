# buildwebpage

## DESCRIPTION

The `buildwebpage` script builds a static webpage by inserting a number of
subpages into a template.

Features:
 * Specification of a title for a subpage which can be referenced by the
   template
 * Assignment of an menu item to a subpage so it can be formatted distinctively
 * Markdown support for subpages


## REQUIREMENTS

 * [Python >=3.2](https://www.python.org/)
 * [Markdown](https://pypi.python.org/pypi/Markdown)


## USAGE

### Creating a webpage

By default the programme looks into the source folder, identifies the template
by its file name and attempts to insert all remaining files in the folder into
the template.

The whole content of a given subpage will be inserted into the template in place
of a `<!-- content -->` comment.  The content itself can be written in html or
in markdown.  For markdown conversion, add a `<!-- markdown -->` comment to
the subpage.

It is also possible to assign a title to a subpage.  A subpage may contain a
comment `<!-- title: SOME TITLE TEXT -->` which will be inserted in place of a
`<!-- title -->` comment in the template.

If the template contains a comment `<!-- modified_date -->', the comment will be
replaced with the date the subpage file was last modified.

Additionally one can mark a specific tag in the template to be the menu item
associated with a subpage by refering to its id using the
`<!-- menu: TAG ID -->` comment.  Any tag that contains the attribute
`id='TAG ID'` will be added a `class='menu-current'` which can then be
formatted using css.


## Command-line Options

    usage: buildwebpage [-h] [-d DIR] [-t FILE] [folder]
    
    positional arguments:
      folder                source folder (default: ./_src/)
    
    optional arguments:
      -h, --help            show this help message and exit
      -d DIR, --dest DIR    destination folder (default: ./)
      -t FILE, --template FILE
                            basename of the template file (default: _template.html)


## LICENSE

Copyright (c) 2013-2015 Johannes Englisch

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
