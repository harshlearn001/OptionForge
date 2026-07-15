import pytest

from optionforge.research.research import Research


def research():

    return Research(
        name="Walk Forward Study",
        strategy_name="Modified PCR",
        description="Institutional validation",
        start_date="2024-01-01",
        end_date="2024-12-31",
        symbol="NIFTY",
        timeframe="1D",
    )


def test_create():

    assert isinstance(
        research(),
        Research,
    )


def test_name():

    assert research().name == "Walk Forward Study"


def test_strategy():

    assert research().strategy_name == "Modified PCR"


def test_symbol():

    assert research().symbol == "NIFTY"


def test_timeframe():

    assert research().timeframe == "1D"


@pytest.mark.parametrize(
    "field",
    [
        "name",
        "strategy_name",
    ],
)
def test_empty(field):

    kwargs = research().to_dict()

    kwargs[field] = ""

    with pytest.raises(ValueError):

        Research(**kwargs)


def test_to_dict():

    data = research().to_dict()

    assert data["symbol"] == "NIFTY"

    assert data["strategy_name"] == "Modified PCR"


def test_str():

    assert "Research" in str(research())


def test_repr():

    assert "Research" in repr(research())
