"""
==============================================================
OptionForge
app/application.py
--------------------------------------------------------------
Professional Application Layer
==============================================================
"""

from __future__ import annotations

from pathlib import Path
from time import perf_counter

from optionforge.config.settings import (
    DEFAULT_SYMBOL,
    LIVE_FOLDER,
)

from optionforge.session import MarketSession


class OptionForgeApp:
    """
    Professional Application Layer.

    Responsibilities
    ----------------
    • Load configuration
    • Start application
    • Measure execution time
    • Handle exceptions
    • Print summary

    This class should NEVER perform analytics.
    """

    @staticmethod
    def run() -> None:

        start = perf_counter()

        try:

            csv_file = LIVE_FOLDER / "sample_option_chain.csv"

            MarketSession.run(csv_file)

            elapsed = perf_counter() - start

            print()
            print("=" * 60)
            print("OPTIONFORGE COMPLETED")
            print("=" * 60)
            print(f"Symbol   : {DEFAULT_SYMBOL}")
            print(f"Runtime  : {elapsed:.2f} sec")
            print("Status   : SUCCESS")

        except Exception as error:

            print()
            print("=" * 60)
            print("OPTIONFORGE FAILED")
            print("=" * 60)
            print(error)
