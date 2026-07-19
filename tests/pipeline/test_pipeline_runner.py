"""
==============================================================
OptionForge
Professional Pipeline Test
==============================================================
"""

from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from optionforge.repository import (
    RepositoryContext,
    RepositoryFactory,
)

from optionforge.utils.loader import Loader

from optionforge.market_snapshot.market_snapshot_builder import (
    MarketSnapshotBuilder,
)

from optionforge.institutional.institutional_snapshot_builder import (
    InstitutionalSnapshotBuilder,
)

from optionforge.pipeline import (
    OptionForgePipeline,
)

print("=" * 60)
print("OPTIONFORGE")
print("PIPELINE TEST")
print("=" * 60)

# ============================================================
# Repository Layer
# ============================================================

context = RepositoryContext(
    marketforge_root=r"H:\MarketForge",
)

factory = RepositoryFactory(context)

# ============================================================
# Loader
# ============================================================

loader = Loader(factory)

market_snapshot_builder = MarketSnapshotBuilder(
    loader,
)

# ============================================================
# Institutional Snapshot Builder
# ============================================================

institutional_snapshot_builder = InstitutionalSnapshotBuilder()

# ============================================================
# Pipeline
# ============================================================

pipeline = OptionForgePipeline(
    snapshot_builder=market_snapshot_builder,
    institutional_snapshot_builder=institutional_snapshot_builder,
)

snapshot = pipeline.execute("NIFTY")

print()
print("Symbol      :", snapshot.symbol)
print("Stage       :", snapshot.stage.name)
print("Option Rows :", snapshot.market_snapshot.option_rows)
print("Future Rows :", snapshot.market_snapshot.future_rows)
print("Spot Rows   :", snapshot.market_snapshot.spot_rows)

print()
print("MISSION COMPLETE")