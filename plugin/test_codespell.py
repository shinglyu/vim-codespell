from unittest.mock import Mock
import sys


# TODO: Move this integration test elsewhere
def test_spell_is_wrong():
    sys.modules['vim'] = Mock()
    sys.modules['vim'].current.buffer = []
    import codespell
    assert codespell.spell_is_wrong("Helro")
    assert not codespell.spell_is_wrong("Hello")


def test_find_spell_errors():
    sys.modules['vim'] = Mock()
    sys.modules['vim'].current.buffer = []
    import codespell
    words = [
        ("Helro", (0, 4)),
        ("world", (6, 10)),
    ]

    assert [("Helro", (0, 4))] == codespell.find_spell_errors(words)
