from optionforge.intelligence.dealer_engine import DealerEngine

print("=" * 60)
print("LONG GAMMA")
print("=" * 60)

print(
    DealerEngine.evaluate(
        spot=25240,
        gamma_flip=25150,
        gamma_exposure=12.5,
        dealer_pressure=4.3,
    )
)

print("\n")

print("=" * 60)
print("SHORT GAMMA")
print("=" * 60)

print(
    DealerEngine.evaluate(
        spot=24800,
        gamma_flip=25000,
        gamma_exposure=-15.4,
        dealer_pressure=-6.2,
    )
)

print("\n")

print("=" * 60)
print("TRANSITION")
print("=" * 60)

print(
    DealerEngine.evaluate(
        spot=25010,
        gamma_flip=25000,
        gamma_exposure=-5.0,
        dealer_pressure=1.0,
    )
)
