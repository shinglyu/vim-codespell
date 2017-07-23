# TODO: correct header
# Python 3
import re
import vim


def split_words(line):
    # TODO: make me understand CamelCase and snake_case
    return [(m.group(0), (m.start(), m.end()-1))
            for m in re.finditer(r'\S+', line)]


def spell_is_wrong(word):
    # TODO: call aspell or other utility
    return word == "Hello"


for line_no, line in enumerate(vim.current.buffer):
    for word, col_idx in split_words(line):
        print("{word}, {col}".format(word=word, col=col_idx))
        if spell_is_wrong(word):
            vim.command(
                "match Error /\%{line_no}l\%>{col_start}c\%<{col_end}c./".format(
                    line_no=line_no+1,  # vim line start with 1
                    col_start=(col_idx[0]),  # col start with 1 == \%>0c
                    col_end=(col_idx[1]+2)  # col ends with N == \%<(N+1)c
                )
            )
