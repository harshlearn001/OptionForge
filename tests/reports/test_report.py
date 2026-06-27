"""
==============================================================
OptionForge
tests/reports/test_report.py
--------------------------------------------------------------
Professional Report Engine Test
==============================================================
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.intelligence import (
    MarketStructure,
    Probability,
    Strategy,
)

from optionforge.reports import ReportEngine


print("=" * 60)
print("OPTIONFORGE")
print("REPORT ENGINE TEST")
print("=" * 60)

# ---------------------------------------------------------
# Market Structure
# ---------------------------------------------------------

market = MarketStructure.calculate(

    support_strength=96,

    resistance_strength=91,

    expected_move=82,

    iv_rank=42,

    iv_percentile=51,

    max_pain=88,

    oi_wall_score=90,

    oi_shift_score=84,

    oi_change_score=80,

)

# ---------------------------------------------------------
# Probability
# ---------------------------------------------------------

probability = Probability.calculate(market)

# ---------------------------------------------------------
# Strategy
# ---------------------------------------------------------

strategy = Strategy.calculate(

    probability=probability,

    spot_price=25000,

    expected_move=692,

)

# ---------------------------------------------------------
# Report
# ---------------------------------------------------------

report = ReportEngine.generate(

    market,

    probability,

    strategy,

)

print()
print(report)
print()

print("MISSION COMPLETE")