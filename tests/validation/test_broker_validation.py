import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE_DIR))

from tests.validation.broker_validation import ValidationResult
from tests.validation.benchmark_report import show

results = [
    ValidationResult(
        metric="Delta",
        broker=0.510,
        optionforge=0.509,
        difference=0.001,
        passed=True,
    ),
    ValidationResult(
        metric="Gamma",
        broker=0.00150,
        optionforge=0.00149,
        difference=0.00001,
        passed=True,
    ),
    ValidationResult(
        metric="Theta",
        broker=-10.70,
        optionforge=-10.66,
        difference=0.04,
        passed=True,
    ),
    ValidationResult(
        metric="Vega",
        broker=11.25,
        optionforge=11.22,
        difference=0.03,
        passed=True,
    ),
    ValidationResult(
        metric="IV",
        broker=9.50,
        optionforge=9.49,
        difference=0.01,
        passed=True,
    ),
]

show(results)
