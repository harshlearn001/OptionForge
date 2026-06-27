import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from optionforge.quant.black_scholes import BlackScholes

print("=" * 60)
print("OPTIONFORGE")
print("BLACK-SCHOLES TEST")
print("=" * 60)

spot = 25000
strike = 25000

# 30 calendar days
time = 30 / 365

# 6%
rate = 0.06

# 20%
volatility = 0.20

call = BlackScholes.call_price(
    spot,
    strike,
    time,
    rate,
    volatility,
)

put = BlackScholes.put_price(
    spot,
    strike,
    time,
    rate,
    volatility,
)

print()
print(f"Spot        : {spot}")
print(f"Strike      : {strike}")
print(f"Volatility  : {volatility:.2%}")
print(f"Time        : {time:.6f}")
print()

print(f"Call Price  : {call:.2f}")
print(f"Put Price   : {put:.2f}")

print()
print("MISSION COMPLETE")