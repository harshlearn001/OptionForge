from optionforge.analytics.pcr.weight_engine import (
    WeightEngine,
)


def test_atm():

    w = WeightEngine()

    assert w.weight(19500, 19500) == 1.0


def test_one_level():

    w = WeightEngine()

    assert w.weight(19550, 19500) == 0.95


def test_two_levels():

    w = WeightEngine()

    assert w.weight(19600, 19500) == 0.90


def test_far():

    w = WeightEngine()

    assert w.weight(20500, 19500) == 0.50


def test_distance():

    w = WeightEngine()

    assert (
        w.distance(
            19650,
            19500,
        )
        == 150
    )


def test_repr():

    w = WeightEngine()

    assert "WeightEngine" in repr(w)
