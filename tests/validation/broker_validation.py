"""
==============================================================
OptionForge
Broker Validation Engine
==============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ValidationResult:

    metric: str

    broker: float

    optionforge: float

    difference: float

    passed: bool
