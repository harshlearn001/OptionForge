from types import SimpleNamespace

from optionforge.kernel.engine_context import EngineContext


def test_context():

    snapshot = SimpleNamespace(
        symbol="NIFTY",
        trade_date=20260716,
        expiry=20260730,
    )

    context = EngineContext(snapshot=snapshot)

    assert context.snapshot.symbol == "NIFTY"