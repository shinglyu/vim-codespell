# TODO: correct header
# Python 3
import re
from subprocess import Popen, PIPE, STDOUT
import vim


def split_words(line):
    # TODO: make me understand CamelCase and snake_case
    return [(m.group(0), (m.start(), m.end()-1))
            for m in re.finditer(r'\S+', line)]

# DEPRECATED! See benchmark results
def spell_is_wrong(word):
    # TODO: call aspell or other utility
    base_aspell_cmd = ['aspell', '-a']
    extra_apsell_args = ["-l", "en-US"]

    cmd = base_aspell_cmd + extra_apsell_args

    p = Popen(cmd,
              stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    stdout = p.communicate(input=str.encode(word))[0]
    output = stdout.decode()
    result_code = output.split("\n")[1][0]
    if result_code == "&":
        return True
    elif result_code == "*":
        return False
    else:
        return True

def find_spell_errors(words):
    base_aspell_cmd = ['aspell', '-a', '--list']
    extra_apsell_args = ["-l", "en-US"]

    cmd = base_aspell_cmd + extra_apsell_args

    p = Popen(cmd,
              stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    word_texts = [x[0] for x in words]

    stdout = p.communicate(input=str.encode(" ".join(word_texts)))[0]
    output = stdout.decode()
    result_codes = [line[0] for line in output.rstrip().split("\n")[1:]] # The first line is a aspell version message
    errors = []
    for code, word in zip(result_codes, words):
        if code == "&":
            errors.append(word)
    return errors


# Main
# TODO: Process all lines at once, add the line no to the words list
for line_no, line in enumerate(vim.current.buffer):
    words = split_words(line)
    for word, col_idx in find_spell_errors(words):
        # TODO: extract this matchadd command as a function
        # print("{word}, {col}".format(word=word, col=col_idx))
        vim.command(
            # "match Error /\%{line_no}l\%>{col_start}c\%<{col_end}c./".format(
            "call matchadd('Error', '\%{line_no}l\%>{col_start}c\%<{col_end}c.')".format(
                line_no=line_no+1,  # vim line start with 1
                col_start=(col_idx[0]),  # col start with 1 == \%>0c
                col_end=(col_idx[1]+2)  # col ends with N == \%<(N+1)c
            )
        )
