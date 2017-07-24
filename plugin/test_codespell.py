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
        "Helro",
        "world",
        "wordd"
    ]

    assert ["Helro", "wordd"] == codespell.find_spell_errors(words)


def test_split_word_plain():
    assert ["Hello", "World"] == codespell.split_words("Hello World")


def test_split_word_underscore():
    assert ["Hello", "World"] == codespell.split_words("Hello_World")
