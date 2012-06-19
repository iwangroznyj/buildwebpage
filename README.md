# buildwebpage

## DESCRIPTION

The `buildwebpage` script builds a static webpage by inserting a number of
subpages into a template.

The template file must contain the word `CONTENT` in capital letters.  This
word will be substituted with the content of the subpage files.  The resulting
web page is then saved in the current working directory.

To avoid filename conflicts all subpage files must be prefixed with `c_`.
Files without that prefix will _not_ be recognised as subpage by the script.

## REQUIREMENTS

This script requires at least Python 2.5.

## USAGE

    buildwebpage.py template subpages ...

