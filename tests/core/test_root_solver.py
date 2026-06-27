import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from optionforge.quant.root_solver import RootSolver

print("=" * 60)
print("OPTIONFORGE")
print("ROOT SOLVER TEST")
print("=" * 60)


def equation(x):

    return x * x - 4


root = RootSolver.bisection(
    equation,
    lower=0,
    upper=5
)

print()

print("Calculated Root :", root)

print("Expected Root   : 2.0")

print()

print("MISSION COMPLETE")