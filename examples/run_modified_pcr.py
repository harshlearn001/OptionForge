"""
============================================================
OptionForge
Run Modified PCR (REAL DATA)
============================================================

Loads REAL MarketForge data and calculates PCR.

Author : OptionForge

============================================================
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from optionforge.analytics.modified_pcr import (
    ModifiedPCREngine,
)

from optionforge.providers.option_provider import (
    OptionProvider,
)

from optionforge.providers.spot_provider import (
    SpotProvider,
)

from optionforge.repository.option_repository import (
    OptionRepository,
)

from optionforge.repository.spot_repository import (
    SpotRepository,
)

from optionforge.repository.repository_context import (
    RepositoryContext,
)

from optionforge.snapshot.institutional_snapshot_builder import (
    SnapshotBuilder,
)


# ============================================================
# Configuration
# ============================================================

MARKETFORGE_ROOT = Path(r"H:\MarketForge")

SYMBOL = "NIFTY"

TRADE_DATE = 20201228

EXPIRY = 20201231


# ============================================================
# Main
# ============================================================

def main():

    print("=" * 60)
    print("OPTIONFORGE")
    print("REAL MARKET DATA TEST")
    print("=" * 60)

    context = RepositoryContext(

        marketforge_root=MARKETFORGE_ROOT,

        use_parquet=True,

        use_cache=True,

        validate_schema=True,

    )

    option_repository = OptionRepository(context)

    spot_repository = SpotRepository(context)

    option_provider = OptionProvider(option_repository)

    spot_provider = SpotProvider(spot_repository)

    builder = SnapshotBuilder(

        option_provider,

        spot_provider,

    )

    snapshot = builder.build(

        symbol=SYMBOL,

        trade_date=TRADE_DATE,

        expiry=EXPIRY,

    )

    engine = ModifiedPCREngine()

    result = engine.calculate(snapshot)

    print()

    print("=" * 60)
    print("MODIFIED PCR REPORT")
    print("=" * 60)

    print(f"Symbol        : {result.symbol}")
    print(f"Trade Date    : {result.trade_date}")
    print(f"Expiry        : {result.expiry}")

    print()

    print(f"Call OI       : {result.call_oi:,.0f}")
    print(f"Put OI        : {result.put_oi:,.0f}")

    print()

    print(f"PCR           : {result.pcr}")

    print(f"Contracts     : {result.contracts:,}")

    print("=" * 60)


if __name__ == "__main__":

    main()