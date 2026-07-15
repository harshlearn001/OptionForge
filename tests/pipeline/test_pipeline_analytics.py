from optionforge.pipeline import OptionForgePipeline


class DummyEngine:
    pass


class DummySnapshotBuilder:
    def build(self, symbol):
        return None


class DummyInstitutionalSnapshotBuilder:
    def build(
        self,
        *,
        market_snapshot,
        analytics=None,
        evidence=None,
        market_dna=None,
        decision=None,
        strategy=None,
        execution=None,
    ):
        return None


def test_pipeline_analytics():

    pipeline = OptionForgePipeline(
        snapshot_builder=DummySnapshotBuilder(),
        institutional_snapshot_builder=DummyInstitutionalSnapshotBuilder(),
        analytics={
            "dummy": DummyEngine(),
        },
    )

    pipeline.analytics()

    assert "registry" in pipeline._context.analytics
    assert "dummy" in pipeline._context.analytics["registry"]

    assert "volatility" in pipeline._context.analytics
    assert "greeks" in pipeline._context.analytics
    assert "oi" in pipeline._context.analytics
    assert "market" in pipeline._context.analytics
