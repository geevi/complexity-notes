


def problem(text, titleline, counter, format):
    s = """ <div class='problem'>
                <b>Problem %s: </b> %s

            </div>
""" % (str(counter), text)
    return s

envir2format = {
#     'intro': {
#         'latex': r"""
# \usepackage{amsthm,tcolorbox}
# \theoremstyle{definition}
# \newtheorem{example}{Example}[section]
# """,},
    'problem': {
        'html': problem
    }
}