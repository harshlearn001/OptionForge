from types import SimpleNamespace

from optionforge.kernel.engine import Engine
from optionforge.kernel.engine_context import EngineContext
from optionforge.kernel.engine_runner import EngineRunner
from optionforge.kernel.registry import Registry


class DummyEngine(Engine):
    """
    Simple engine used for runtime testing.
    """

    def execute(
        self,
        snapshot,
    ):

        return {
            "status": "OK",
            "symbol": snapshot.symbol,
        }


def test_engine_runner():

    snapshot = SimpleNamespace(
        symbol="NIFTY",
        trade_date=20260716,
        expiry=20260730,
    )

    context = EngineContext(
        snapshot=snapshot,
    )

    registry = Registry()

    registry.register(
        DummyEngine(),
    )

    runner = EngineRunner(
        registry,
    )

    results = runner.execute(
        context,
    )

    assert len(results) == 1

    assert results.exists(
        "DummyEngine",
    )

    execution = results.get(
        "DummyEngine",
    )

    assert execution.succeeded

    assert execution.result["status"] == "OK"

    assert execution.result["symbol"] == "NIFTY"

    assert execution.duration >= 0