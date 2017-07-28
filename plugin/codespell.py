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
    script_dir = vim.eval("s:dir")
    return find_spell_errors(words, ["-d", "cs.dict", "--dict-dir={dir}/../dict".format(dir=script_dir)])

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
    # silently skip empty string, which is usually due to the dictionary not
    # working correctly
    if len(word) == 0:
        continue
    # We ignore words that has more lowercase char after it, because we
    # might be matching a prefix.
    if word[0].isupper():
        # If the word starts with a upper case, it might be part of a CamelCase
        # word, so we need to allow characters before it.
        # TODO: extract this matchadd command as a function
        vim.command(
            "call matchadd(\'Error\', \'\\v{word}\ze[^a-z]\')".format(
                word=re.escape(word)
            )
        )
    else:
        # If the word starts with a lower case, we don't allow any lowercase
        # charater before it, becuase the match may be a suffix
        vim.command(
            "call matchadd(\'Error\', \'\\v[^a-z]\zs{word}\ze[^a-z]\')".format(
                word=re.escape(word)
            )
        )
