import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from optionforge.quant.greeks import Greeks

print("=" * 60)
print("OPTIONFORGE")
print("GREEKS TEST")
print("=" * 60)

spot = 25000
strike = 25000
time = 30 / 365
rate = 0.06
volatility = 0.20

delta = Greeks.delta(
    spot,
    strike,
    time,
    rate,
    volatility,
    "CE",
)

gamma = Greeks.gamma(
    spot,
    strike,
    time,
    rate,
    volatility,
    "CE",
)

theta = Greeks.theta(
    spot,
    strike,
    time,
    rate,
    volatility,
    "CE",
)

vega = Greeks.vega(
    spot,
    strike,
    time,
    rate,
    volatility,
    "CE",
)

print()

print(f"Delta : {delta:.6f}")
print(f"Gamma : {gamma:.8f}")
print(f"Theta : {theta:.4f}")
print(f"Vega  : {vega:.4f}")

print()
print("MISSION COMPLETE")
