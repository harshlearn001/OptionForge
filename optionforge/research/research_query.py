"""
==============================================================
OptionForge
Research Query
==============================================================

Immutable research query used by the Research Engine.

Represents the complete market snapshot that will be
matched against historical data.

Author
------
OptionForge Engineering Team
==============================================================
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass

from optionforge.common.enums import TrendDirection

from optionforge.intelligence.enums.dealer_state import DealerState
from optionforge.intelligence.enums.institutional_state import InstitutionalState
from optionforge.intelligence.enums.volatility_state import VolatilityState

from optionforge.regime.enums.regime_state import RegimeState


@dataclass(slots=True, frozen=True)
class ResearchQuery:
    """
    Immutable research query.
    """

    symbol: str

    regime: RegimeState

    institutional_state: InstitutionalState

    dealer_state: DealerState

    trend: TrendDirection

    volatility: VolatilityState

    iv_rank: float

    iv_percentile: float

    pcr: float

    def to_dict(self) -> dict:
        """
        Dictionary representation.
        """

        d = asdict(self)

        d["regime"] = self.regime.name
        d["institutional_state"] = self.institutional_state.name
        d["dealer_state"] = self.dealer_state.name
        d["trend"] = self.trend.name
        d["volatility"] = self.volatility.name

        return d

    def summary(self) -> dict:
        """
        Lightweight summary.
        """

        return {

            "symbol": self.symbol,

            "regime": self.regime.name,

            "institutional": self.institutional_state.name,

            "dealer": self.dealer_state.name,

        }

    def __repr__(self) -> str:

        return (

            "ResearchQuery("

            f"{self.symbol}, "

            f"{self.regime.name})"

        )