"""
==============================================================
OptionForge
intelligence/gamma_flip.py
--------------------------------------------------------------
Gamma Flip Intelligence Engine
==============================================================
"""

from __future__ import annotations

from optionforge.models import (
    GammaExposureResult,
    GammaFlipResult,
)


class GammaFlip:
    """
    Professional Gamma Flip Intelligence Engine.
    """

    @staticmethod
    def calculate(
        *,
        gamma: GammaExposureResult,
        current_spot: float,
    ) -> GammaFlipResult:

        flip = gamma.gamma_flip

        distance = round(current_spot - flip, 2)

        # --------------------------------------------------
        # Flip Status
        # --------------------------------------------------

        if current_spot > flip:

            flip_status = "ABOVE GAMMA FLIP"

        elif current_spot < flip:

            flip_status = "BELOW GAMMA FLIP"

        else:

            flip_status = "AT GAMMA FLIP"

        # --------------------------------------------------
        # Dealer Regime
        # --------------------------------------------------

        if current_spot >= flip:

            dealer_regime = "POSITIVE GAMMA"

            interpretation = (
                "Spot is above the Gamma Flip. "
                "Dealers are more likely to dampen volatility "
                "and stabilize price movement."
            )

        else:

            dealer_regime = "NEGATIVE GAMMA"

            interpretation = (
                "Spot is below the Gamma Flip. "
                "Dealers may amplify directional moves, "
                "leading to higher volatility."
            )

        return GammaFlipResult(

            gamma_flip=flip,

            current_spot=current_spot,

            distance=distance,

            flip_status=flip_status,

            dealer_regime=dealer_regime,

            interpretation=interpretation,

        )