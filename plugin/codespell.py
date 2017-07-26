# TODO: correct header
# Python 3
from collections import defaultdict
import re
from subprocess import Popen, PIPE, STDOUT
import vim


def tokenize(line):
    words = [m.group(0) for m in re.finditer(r"[a-zA-Z]+", line)]
    # TODO: maybe merge the two regex or make this more efficient
    final_words = []
    for word in words:
        # Ref: https://stackoverflow.com/questions/29916065/how-to-do-camelcase-split-in-python
        final_words += [m.group(0) for m in re.finditer(".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", word)]

    return final_words


def filter_multi_occurance(words):
    counts = defaultdict(lambda: 0)
    for word in words:
        counts[word] += 1
    filtered = []
    for word, count in counts.items():
        # TODO: make this configurable
        if count < 5:
            filtered.append(word)
    return filtered


def find_spell_errors_cs(words):
    # Must be executed from the top level
    return find_spell_errors(words, ["-d", "cs.dict", "--dict-dir=./dict"])

def find_spell_errors(words, extra_args=[]):
    base_aspell_cmd = ["aspell", "--list"]
    extra_aspell_args = ["-l", "en-US"]

    cmd = base_aspell_cmd + extra_aspell_args + extra_args

    p = Popen(cmd,
              stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    stdout = p.communicate(input=str.encode(" ".join(words)))[0]
    output = stdout.decode()
    return output.rstrip().split("\n")


# Main
lines = " ".join(vim.current.buffer)
words = tokenize(lines)
words = filter_multi_occurance(words)
unique_words = list(set(words))
for word in find_spell_errors(find_spell_errors_cs(unique_words)):
    # TODO: extract this matchadd command as a function
    vim.command(
        # We ignore words that has more lowercase char after it, becase we
        # might be matching a prefix.
        "call matchadd(\'Error\', \'\\v{word}\ze[^a-z]\')".format(
            word=re.escape(word)
        )
    )
