from optionforge.integration.file_resolver import FileResolver
from optionforge.integration.validator import MarketValidator


def test_imports():
    assert FileResolver is not None
    assert MarketValidator is not None
