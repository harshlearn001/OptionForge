from pathlib import Path

from optionforge.integration.file_resolver import FileResolver


def build_resolver():

    return FileResolver(
        option_root=Path(r"H:\MarketForge\data\master\option_master"),
        index_spot_root=Path(r"H:\MarketForge\data\master\Indices_master"),
        equity_spot_root=Path(r"H:\MarketForge\data\master\Equity_stock_master"),
    )


def test_resolver_creation():
    resolver = build_resolver()
    assert resolver is not None


def test_option_path():
    resolver = build_resolver()
    path = resolver.resolve_option("NIFTY")
    assert path.exists()


def test_index_path():
    resolver = build_resolver()
    path = resolver.resolve_index_spot("NIFTY")
    assert path.exists()


def test_equity_path():
    resolver = build_resolver()
    path = resolver.resolve_equity_spot("RELIANCE")
    assert path.exists()