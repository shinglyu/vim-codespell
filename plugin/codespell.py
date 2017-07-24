# TODO: correct header
# Python 3
import re
from subprocess import Popen, PIPE, STDOUT
import vim


def split_words(line):
    # TODO: make me understand CamelCase and snake_case
    # re column index start with 0, vim index start with 1
    return [m.group(0) for m in re.finditer(r"[^_^\s^\.^=]+", line)] #^_: not underscore, ^\s: not whitespace


# DEPRECATED! See benchmark results
def spell_is_wrong(word):
    # TODO: call aspell or other utility
    base_aspell_cmd = ["aspell", "-a"]
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
    base_aspell_cmd = ["aspell", "--list"]
    extra_apsell_args = ["-l", "en-US"]

    cmd = base_aspell_cmd + extra_apsell_args

    p = Popen(cmd,
              stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    stdout = p.communicate(input=str.encode(" ".join(words)))[0]
    output = stdout.decode()
    return output.rstrip().split("\n")


# Main
lines = " ".join(vim.current.buffer)
words = split_words(lines)
unique_words = list(set(words))
for word in find_spell_errors(unique_words):
    # TODO: extract this matchadd command as a function
    vim.command(
        "call matchadd(\"Error\", \"{word}\")".format(
            word=re.escape(word)
        )
    )
