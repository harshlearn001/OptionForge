"""
==============================================================
OptionForge
Intelligence
Base Intelligence Result
==============================================================

Immutable base object returned by every
Institutional Intelligence engine.

Author : OptionForge
==============================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class IntelligenceResult:
    """
    Base result produced by every intelligence engine.

    Every intelligence engine should explain:

    • What is the conclusion?
    • How confident are we?
    • Why?
    • What are the risks?
    """

    confidence: float

    evidence: tuple[str, ...]

    risks: tuple[str, ...]

    summary: str

    def __post_init__(self) -> None:

        if not (0.0 <= self.confidence <= 100.0):
            raise ValueError("confidence must be between 0 and 100")
