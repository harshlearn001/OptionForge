"""
==============================================================
OptionForge
Run Complete Test Suite
==============================================================
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


TESTS = [

    # ---------------------------------------------------------
    # CORE
    # ---------------------------------------------------------

    "tests/core/test_distribution.py",

    "tests/core/test_root_solver.py",

    "tests/core/test_black_scholes.py",

    "tests/core/test_iv.py",

    "tests/core/test_greeks.py",

    # ---------------------------------------------------------
    # MODELS
    # ---------------------------------------------------------

    "tests/models/test_option_contract.py",

    "tests/models/test_market_snapshot.py",

    # ---------------------------------------------------------
    # ANALYTICS
    # ---------------------------------------------------------

    "tests/analytics/test_analytics.py",

    "tests/analytics/test_option_chain.py",

    # ---------------------------------------------------------
    # STORAGE
    # ---------------------------------------------------------

    "tests/storage/test_storage.py",

    # ---------------------------------------------------------
    # VALIDATION
    # ---------------------------------------------------------

    "tests/validation/test_broker_validation.py",

    # ---------------------------------------------------------
    # INTEGRATION
    # ---------------------------------------------------------

    "tests/integration/test_pipeline.py",

    "tests/intelligence/test_expected_move.py",

    "tests/intelligence/test_iv_rank.py",

    "tests/intelligence/test_iv_percentile.py",

    "tests/intelligence/test_max_pain.py",

    "tests/intelligence/test_oi_wall.py",

    "tests/intelligence/test_oi_change.py",

    "tests/intelligence/test_oi_shift.py",

    "tests/intelligence/test_support_strength.py",

    "tests/intelligence/test_resistance_strength.py",

    "tests/intelligence/test_market_structure.py",

    "tests/intelligence/test_probability.py",

    "tests/intelligence/test_strategy.py",

    "tests/reports/test_report.py",

    "tests/dashboard/test_dashboard.py",

    "tests/intelligence/test_scanner.py",

    "tests/datasource/test_market_data.py",

    "tests/storage/test_schema.py",
    
]

print("=" * 65)
print("OPTIONFORGE COMPLETE TEST SUITE")
print("=" * 65)

passed = 0

failed = 0

for test in TESTS:

    print()
    print("-" * 65)
    print(test)
    print("-" * 65)

    result = subprocess.run(
        [sys.executable, str(ROOT / test)]
    )

    if result.returncode == 0:

        passed += 1

    else:

        failed += 1

print()
print("=" * 65)

print("TOTAL TESTS :", len(TESTS))

print("PASSED      :", passed)

print("FAILED      :", failed)

print("=" * 65)

if failed == 0:

    print("OPTIONFORGE STATUS : ALL TESTS PASSED")

else:

    print("OPTIONFORGE STATUS : SOME TESTS FAILED")