from optionforge.intelligence.decision_engine import DecisionEngine

from optionforge.intelligence.enums.dealer_state import DealerState
from optionforge.intelligence.enums.market_state import MarketState

from optionforge.intelligence.models.dealer_intelligence import (
    DealerIntelligence,
)
from optionforge.intelligence.models.market_intelligence import (
    MarketIntelligence,
)


dealer = DealerIntelligence(

    state=DealerState.LONG_GAMMA,

    confidence=95.0,

    evidence=("Positive Gamma",),

    risks=("Watch Gamma Flip",),

    summary="Dealers are long gamma.",

)

market = MarketIntelligence(

    state=MarketState.BULLISH_TREND,

    confidence=90.0,

    evidence=("Bullish Structure",),

    risks=("Resistance Ahead",),

    summary="Market is bullish.",

)

decision = DecisionEngine.evaluate(

    dealer=dealer,

    market=market,

)

print()
print("=" * 60)
print("INSTITUTIONAL DECISION")
print("=" * 60)
print(decision)
print("=" * 60)

assert decision.state == decision.state.STRONGLY_BULLISH

print("\nPASS : Decision Engine Test Successful")