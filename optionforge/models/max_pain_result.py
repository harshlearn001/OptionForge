"""
==============================================================
OptionForge
models/max_pain_result.py
--------------------------------------------------------------
Professional Max Pain Result
==============================================================
"""

from dataclasses import dataclass
import pandas as pd


@dataclass(slots=True)
class MaxPainResult:

    max_pain: float

    total_pain: float

    call_pain: float

    put_pain: float

    evaluated_strikes: int

    support: float

    resistance: float

    highest_call_oi: float

    highest_put_oi: float

    total_call_oi: int

    total_put_oi: int

    pain_table: pd.DataFrame

    interpretation: str