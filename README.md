# buildwebpage

## DESCRIPTION

The `buildwebpage` script builds a static webpage by inserting a number of
subpages into a template.

The template file must contain the comment `<!--CONTENT-->`.  This comment will
be substituted by the content of the subpage files.

By default the script treats all files in the current directory as subpages
that begin with an underscore `_`.  This behaviour can be overwritten by adding
subpage files as command line arguments.

## REQUIREMENTS

This script requires at least Python 2.5.

## USAGE

    buildwebpage.py template [subpages ...]

