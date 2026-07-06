from optionforge.intelligence.enums.dealer_state import DealerState
from optionforge.intelligence.models.dealer_intelligence import DealerIntelligence

dealer = DealerIntelligence(
    state=DealerState.LONG_GAMMA,
    confidence=87.5,
    evidence=("Positive Gamma Exposure",),
    risks=("Gamma Flip Below Spot",),
    summary="Dealers are likely long gamma.",
)

print(dealer)