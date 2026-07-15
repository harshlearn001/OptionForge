from __future__ import annotations

from optionforge.common.enums import OptionType
from optionforge.market.option_chain import OptionChain

from tests.fixtures.snapshot_fixture import build_snapshot


def build_option_chain() -> OptionChain:

    snapshots = (
        build_snapshot(
            strike_price=24950,
            option_type=OptionType.CALL,
            open_interest=900,
        ),
        build_snapshot(
            strike_price=24950,
            option_type=OptionType.PUT,
            open_interest=1800,
        ),
        build_snapshot(
            strike_price=25000,
            option_type=OptionType.CALL,
            open_interest=2500,
        ),
        build_snapshot(
            strike_price=25000,
            option_type=OptionType.PUT,
            open_interest=2300,
        ),
        build_snapshot(
            strike_price=25050,
            option_type=OptionType.CALL,
            open_interest=1700,
        ),
        build_snapshot(
            strike_price=25050,
            option_type=OptionType.PUT,
            open_interest=1200,
        ),
    )

    return OptionChain(snapshots)
