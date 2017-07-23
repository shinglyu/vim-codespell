from unittest.mock import Mock
import sys

# TODO: Move this integration test elsewhere
def test_spell_is_wrong():
    sys.modules['vim'] = Mock()
    sys.modules['vim'].current.buffer = []
    import codespell
    assert True == codespell.spell_is_wrong("Helro")
    assert False == codespell.spell_is_wrong("Hello")

