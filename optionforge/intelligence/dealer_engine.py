"""
==============================================================
OptionForge
Intelligence
Dealer Intelligence Engine
==============================================================

Interprets dealer positioning from market analytics.

Version : 1.2
Author  : OptionForge
==============================================================
"""

from __future__ import annotations

from optionforge.intelligence.enums.dealer_state import DealerState
from optionforge.intelligence.models.dealer_intelligence import (
    DealerIntelligence,
)


class DealerEngine:
    """
    Dealer Intelligence Engine.

    Produces an institutional interpretation of
    dealer positioning.

    Inputs
    ------
    • Spot
    • Gamma Flip
    • Gamma Exposure
    • Dealer Pressure

    Future Versions
    ---------------
    • Zero Gamma
    • Vanna
    • Charm
    • IV Regime
    • OI Migration
    """

    LONG_CONFIDENCE = 95.0
    SHORT_CONFIDENCE = 95.0
    TRANSITION_CONFIDENCE = 65.0

    @classmethod
    def evaluate(
        cls,
        *,
        spot: float,
        gamma_flip: float,
        gamma_exposure: float,
        dealer_pressure: float,
    ) -> DealerIntelligence:

        evidence: list[str] = []

        # ---------------------------------------------------------
        # Evidence
        # ---------------------------------------------------------

        evidence.append(
            f"Gamma Exposure = {gamma_exposure:.2f}"
        )

        evidence.append(
            f"Dealer Pressure = {dealer_pressure:.2f}"
        )

        if spot >= gamma_flip:

            evidence.append(
                f"Spot ({spot:.2f}) above Gamma Flip ({gamma_flip:.2f})"
            )

        else:

            evidence.append(
                f"Spot ({spot:.2f}) below Gamma Flip ({gamma_flip:.2f})"
            )

        # ---------------------------------------------------------
        # Signal Agreement
        # ---------------------------------------------------------

        agreement = 0

        if gamma_exposure > 0:
            agreement += 1
        elif gamma_exposure < 0:
            agreement -= 1

        if dealer_pressure > 0:
            agreement += 1
        elif dealer_pressure < 0:
            agreement -= 1

        if spot >= gamma_flip:
            agreement += 1
        else:
            agreement -= 1

        # ---------------------------------------------------------
        # Institutional Interpretation
        # ---------------------------------------------------------

        if agreement == 3:

            state = DealerState.LONG_GAMMA

            confidence = cls.LONG_CONFIDENCE

            summary = (
                "All dealer signals align toward a LONG GAMMA regime."
            )

            risks = (
                "A sustained move below Gamma Flip may invalidate this view.",
            )

        elif agreement == -3:

            state = DealerState.SHORT_GAMMA

            confidence = cls.SHORT_CONFIDENCE

            summary = (
                "All dealer signals align toward a SHORT GAMMA regime."
            )

            risks = (
                "Recovery above Gamma Flip may invalidate this view.",
            )

        else:

            state = DealerState.TRANSITION

            confidence = cls.TRANSITION_CONFIDENCE

            summary = (
                "Dealer signals are mixed. The market is currently "
                "transitioning between regimes."
            )

            risks = (
                "Conflicting dealer signals reduce confidence.",
            )

        return DealerIntelligence(
            state=state,
            confidence=confidence,
            evidence=tuple(evidence),
            risks=risks,
            summary=summary,
        )