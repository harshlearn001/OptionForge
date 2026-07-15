"""
============================================================
OptionForge
Gamma Exposure Calculator
============================================================

Institutional Gamma Exposure Calculator

============================================================
"""

from __future__ import annotations


class GammaExposureCalculator:
    """
    Calculate Gamma Exposure (GEX).
    """

    @staticmethod
    def calculate(
        *,
        gamma: float,
        open_interest: int,
        contract_size: int,
        spot: float,
    ) -> float:

        if gamma < 0:
            raise ValueError("gamma cannot be negative.")

        if open_interest < 0:
            raise ValueError("open_interest cannot be negative.")

        if contract_size <= 0:
            raise ValueError("contract_size must be positive.")

        if spot <= 0:
            raise ValueError("spot must be positive.")

        return gamma * open_interest * contract_size * (spot**2) * 0.01

    def __repr__(self):

        return "GammaExposureCalculator()"

    __str__ = __repr__
