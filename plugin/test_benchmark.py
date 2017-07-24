from unittest.mock import Mock
import sys
from subprocess import Popen, PIPE, STDOUT

sys.modules['vim'] = Mock()
sys.modules['vim'].current.buffer = []
import codespell

text = "On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."


def test_every_word_speed(benchmark):
    @benchmark
    def check_paragraph():
        for word in text.split():
            # codespell.spell_is_wrong(word)
            base_aspell_cmd = ['aspell', '-a']
            extra_apsell_args = ["-l", "en-US"]

            cmd = base_aspell_cmd + extra_apsell_args

            p = Popen(cmd,
                    stdout=PIPE, stdin=PIPE, stderr=STDOUT)
            stdout = p.communicate(input=str.encode(word))[0]
            output = stdout.decode()
            result_code = output.split("\n")[1][0]

def test_all_words_list(benchmark):
    @benchmark
    def check_paragraph():
        # codespell.spell_is_wrong(word)
        base_aspell_cmd = ['aspell', '-a', '--list']
        extra_apsell_args = ["-l", "en-US"]

        cmd = base_aspell_cmd + extra_apsell_args

        p = Popen(cmd,
                stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        stdout = p.communicate(input=str.encode(text))[0]
        output = stdout.decode()
        result_code = output.split("\n")[1][0]

def test_all_words_list_sort(benchmark):
    @benchmark
    def check_paragraph():
        # codespell.spell_is_wrong(word)
        words = sorted(text.split())

        base_aspell_cmd = ['aspell', '-a', '--list']
        extra_apsell_args = ["-l", "en-US"]

        cmd = base_aspell_cmd + extra_apsell_args

        p = Popen(cmd,
                stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        stdout = p.communicate(input=str.encode(" ".join(words)))[0]
        output = stdout.decode()
        result_code = output.split("\n")[1][0]

def test_all_words_list_sort_unique(benchmark):
    @benchmark
    def check_paragraph():
        # codespell.spell_is_wrong(word)
        seen = set()
        words = [x for x in text.split() if not (x in seen or seen.add(x))]

        base_aspell_cmd = ['aspell', '-a', '--list']
        extra_apsell_args = ["-l", "en-US"]

        cmd = base_aspell_cmd + extra_apsell_args

        p = Popen(cmd,
                stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        stdout = p.communicate(input=str.encode(" ".join(words)))[0]
        output = stdout.decode()
        result_code = output.split("\n")[1][0]

