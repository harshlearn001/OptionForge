from optionforge.intelligence.enums.volatility_state import (
    VolatilityState,
)

from optionforge.intelligence.models.volatility_intelligence import (
    VolatilityIntelligence,
)

volatility = VolatilityIntelligence(
    state=VolatilityState.CHEAP,
    confidence=88.0,
    evidence=(
        "IV Rank below historical average",
        "IV Percentile below median",
    ),
    risks=("Volatility expansion possible",),
    summary=("Options appear relatively inexpensive."),
)

print(volatility)
