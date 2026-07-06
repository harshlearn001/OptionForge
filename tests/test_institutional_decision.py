from optionforge.intelligence.enums.institutional_state import (
    InstitutionalState,
)

from optionforge.intelligence.models.institutional_decision import (
    InstitutionalDecision,
)


decision = InstitutionalDecision(

    state=InstitutionalState.STRONGLY_BULLISH,

    confidence=95.0,

    evidence=(
        "Dealer is LONG GAMMA",
        "Market is BULLISH",
    ),

    risks=(
        "Resistance overhead",
    ),

    summary=(
        "Institutional conditions strongly favor a bullish view."
    ),

)

print(decision)