# buildwebpage.py

## DESCRIPTION

This script generates a static website with several subsites.  This is done by
inserting the content of the subsites into a template file.

In the template file there is a line containing the word CONTENT in capital
letters.  The `buildwebpage` script replaces this whole line with the content
of the

## REQUIREMENTS

This script requires at least Python 2.5.

## USAGE

    buildwebpage.py template content ...

content files:  The file name of the content files must be prefixed with `c_`
                to be recognised by the script.

