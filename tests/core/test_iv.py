import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from optionforge.quant.black_scholes import BlackScholes
from optionforge.quant.implied_volatility import ImpliedVolatility

print("=" * 60)
print("OPTIONFORGE")
print("IMPLIED VOLATILITY TEST")
print("=" * 60)

spot = 25000
strike = 25000

time = 30 / 365

rate = 0.06

true_volatility = 0.20

market_price = BlackScholes.call_price(
    spot,
    strike,
    time,
    rate,
    true_volatility,
)

iv = ImpliedVolatility.call_iv(
    market_price,
    spot,
    strike,
    time,
    rate,
)

print()

print(f"Original Volatility : {true_volatility:.4f}")

print(f"Recovered IV        : {iv:.4f}")

print()

print("MISSION COMPLETE")
