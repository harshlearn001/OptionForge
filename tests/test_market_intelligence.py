from optionforge.intelligence.enums.market_state import MarketState
from optionforge.intelligence.models.market_intelligence import (
    MarketIntelligence,
)

market = MarketIntelligence(
    state=MarketState.BULLISH_TREND,
    confidence=90.0,
    evidence=(
        "Price above trend",
        "Support holding",
    ),
    risks=(
        "Resistance nearby",
    ),
    summary="Market remains in a bullish trend.",
)

print(market)