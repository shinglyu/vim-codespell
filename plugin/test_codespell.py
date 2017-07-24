from unittest.mock import Mock
import sys

sys.modules['vim'] = Mock()
sys.modules['vim'].current.buffer = []
import codespell


# TODO: Move this integration test elsewhere
def test_spell_is_wrong():
    assert codespell.spell_is_wrong("Helro")
    assert not codespell.spell_is_wrong("Hello")


def test_find_spell_errors():
    words = [
        ("Helro", (0, 4)),
        ("world", (6, 10)),
    ]

    assert [("Helro", (0, 4))] == codespell.find_spell_errors(words)


def test_split_word_plain():
    assert [("Hello", (1, 5)), ("World", (7, 11))] == codespell.split_words("Hello World")

def test_split_word_underscore():
    assert [("Hello", (1, 5)), ("World", (7, 11))] == codespell.split_words("Hello_World")
