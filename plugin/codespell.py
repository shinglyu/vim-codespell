# TODO: correct header
# Python 3
import re
from subprocess import Popen, PIPE, STDOUT
import vim


def split_words(line):
    # TODO: make me understand CamelCase and snake_case
    return [(m.group(0), (m.start(), m.end()-1))
            for m in re.finditer(r'\S+', line)]


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


# Main
for line_no, line in enumerate(vim.current.buffer):
    # This for loop is slow, can we use the --list mode of aspell?
    for word, col_idx in split_words(line):
        #print("{word}, {col}".format(word=word, col=col_idx))
        if spell_is_wrong(word):
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
