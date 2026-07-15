"""
============================================================
OptionForge
Intelligence Rule Tests
============================================================
"""

import pytest

from optionforge.intelligence.rules.intelligence_rule import (
    IntelligenceRule,
)


def test_rule_is_abstract():
    """
    IntelligenceRule cannot be instantiated directly.
    """

    with pytest.raises(TypeError):

        IntelligenceRule()
