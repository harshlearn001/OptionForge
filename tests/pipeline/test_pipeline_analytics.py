from optionforge.utils.loader import Loader
from optionforge.pipeline import OptionForgePipeline


class DummyEngine:
    pass


def test_pipeline_analytics():

    pipeline = OptionForgePipeline(
        loader=Loader(),
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