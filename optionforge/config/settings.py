"""
==============================================================
OptionForge
config/settings.py
--------------------------------------------------------------
Professional Configuration
==============================================================
"""

from pathlib import Path

# ==========================================================
# PROJECT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ==========================================================
# DATA
# ==========================================================

DATA_FOLDER = PROJECT_ROOT / "data"

LIVE_FOLDER = DATA_FOLDER / "live"

EXAMPLES_FOLDER = PROJECT_ROOT / "examples"

# ==========================================================
# OUTPUT
# ==========================================================

OUTPUT_FOLDER = PROJECT_ROOT / "output"

RUNTIME_FOLDER = PROJECT_ROOT / "optionforge" / "runtime"

# ==========================================================
# DEFAULTS
# ==========================================================

DEFAULT_SYMBOL = "NIFTY"

REPORT_FORMAT = "txt"

# ==========================================================
# SAVE OPTIONS
# ==========================================================

SAVE_REPORT = True

SAVE_DASHBOARD = True

SAVE_SCANNER = True

SAVE_ANALYTICS = True

SAVE_PARQUET = True
