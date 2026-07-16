from types import SimpleNamespace

from optionforge.kernel.engine import Engine
from optionforge.kernel.engine_context import EngineContext
from optionforge.kernel.engine_runner import EngineRunner
from optionforge.kernel.registry import Registry


class EngineA(Engine):
    def execute(self, snapshot):
        return "A"


class EngineB(Engine):
    def execute(self, snapshot):
        return "B"


class EngineC(Engine):
    def execute(self, snapshot):
        return "C"


def test_runtime_integration():

    snapshot = SimpleNamespace(
        symbol="NIFTY",
        trade_date=20260716,
        expiry=20260730,
    )

    context = EngineContext(snapshot=snapshot)

    registry = Registry()

    registry.register(EngineA())
    registry.register(EngineB())
    registry.register(EngineC())

    runner = EngineRunner(registry)

    results = runner.execute(context)

    assert len(results) == 3

    assert results.exists("EngineA")
    assert results.exists("EngineB")
    assert results.exists("EngineC")

    assert results.get("EngineA").result == "A"
    assert results.get("EngineB").result == "B"
    assert results.get("EngineC").result == "C"

    assert all(result.succeeded for result in results)