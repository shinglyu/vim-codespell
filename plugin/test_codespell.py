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


# Disabled because this is the default behavior of aspell
#def test_aspell_alphanumeric():
#    words = [ "tos2" ]
#
#    assert ["tos"] != codespell.find_spell_errors(words)
#    assert ["tos2"] == codespell.find_spell_errors(words)

def test_find_spell_errors_cs():
    words = [
        "http",
        "hello",
    ]

    assert ["hello"] == codespell.find_spell_errors_cs(words)


def test_tokenize_plain():
    assert ["Hello", "World"] == codespell.tokenize("Hello World")


def test_tokenize_underscore():
    assert ["Hello", "World"] == codespell.tokenize("Hello_World")


def test_tokenize_brackets():
    assert ["Hello", "World"] == codespell.tokenize("Hello(World)")
    assert ["Hello", "World"] == codespell.tokenize("Hello[World]")
    assert ["Hello", "World"] == codespell.tokenize("Hello{World}")
    assert ["Hello", "World"] == codespell.tokenize("Hello<World>")


def test_tokenize_quotes():
    assert ["Hello", "World"] == codespell.tokenize("Hello\"World\"")
    assert ["Hello", "World"] == codespell.tokenize("Hello\'World\'")
    assert ["Hello", "World"] == codespell.tokenize("Hello \'World\'")


def test_tokenize_pointers():
    assert ["pointer"] == codespell.tokenize("*pointer")
    assert ["pointer"] == codespell.tokenize("&pointer")
    assert ["pointer"] == codespell.tokenize("&&*pointer")


def test_tokenize_camel_case():
    assert ["camel", "Case"] == codespell.tokenize("camelCase")
    assert ["Title", "Case"] == codespell.tokenize("TitleCase")
    assert ["Title", "Case", "mixed"] == codespell.tokenize("TitleCase mixed")


def test_tokenize_namespace():
    assert ["std", "mem"] == codespell.tokenize("std::mem")
    assert ["std", "mem"] == codespell.tokenize("std:mem")


def test_tokenize_alphanumeric():
    assert ["uzer"] == codespell.tokenize("uzer42")


def test_filter_multi_occurance():
    assert ["Hello"] == codespell.filter_multi_occurance(["Hello"] + ["World"] * 5)
