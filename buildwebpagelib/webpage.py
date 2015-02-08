from os import mkdir
from os.path import join, isdir, basename


def create_webpage(templ, subpages, destination):
    if not isdir(destination):
        mkdir(destination)
    for subpage in subpages:
        output_file = join(destination, basename(subpage.filename))
        composed = templ.insert_subpage(subpage)
        print(templ.filename, ' + ', subpage.filename, ' => ', output_file)
        try:
            with open(output_file, 'w') as f:
                f.write(composed)
        except IOError as error:
            warning.warnf(error)
