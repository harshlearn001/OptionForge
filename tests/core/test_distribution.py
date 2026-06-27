import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from optionforge.quant.distributions import NormalDistribution


print("=" * 60)
print("OPTIONFORGE")
print("NORMAL DISTRIBUTION TEST")
print("=" * 60)

print()

print("PDF(0) =", NormalDistribution.pdf(0))

print("CDF(0) =", NormalDistribution.cdf(0))

print()

print("Expected")

print("PDF(0) ≈ 0.39894228")

print("CDF(0) = 0.5")