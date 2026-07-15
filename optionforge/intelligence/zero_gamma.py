"""
==============================================================
OptionForge
intelligence/zero_gamma.py
--------------------------------------------------------------
Zero Gamma Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    GammaExposureResult,
    ZeroGammaResult,
)


class ZeroGamma:
    """
    Professional Zero Gamma Intelligence Engine.
    """

    @staticmethod
    def calculate(
        *,
        gamma: GammaExposureResult,
        current_spot: float,
    ) -> ZeroGammaResult:

        zero_gamma = gamma.gamma_flip

        distance = round(current_spot - zero_gamma, 2)

        # --------------------------------------------------
        # Status
        # --------------------------------------------------

        if current_spot > zero_gamma:

            status = "ABOVE ZERO GAMMA"

        elif current_spot < zero_gamma:

            status = "BELOW ZERO GAMMA"

        else:

            status = "AT ZERO GAMMA"

        # --------------------------------------------------
        # Dealer Regime
        # --------------------------------------------------

        if current_spot >= zero_gamma:

            dealer_regime = "STABLE"

            interpretation = (
                "Spot is above the Zero Gamma level. "
                "Dealer hedging is more likely to stabilize "
                "price movements and suppress volatility."
            )

        else:

            dealer_regime = "UNSTABLE"

            interpretation = (
                "Spot is below the Zero Gamma level. "
                "Dealer hedging may reinforce market moves, "
                "increasing directional volatility."
            )

        return ZeroGammaResult(
            zero_gamma=zero_gamma,
            current_spot=current_spot,
            distance=distance,
            status=status,
            dealer_regime=dealer_regime,
            interpretation=interpretation,
        )
