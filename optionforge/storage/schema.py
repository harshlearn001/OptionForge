"""
==============================================================
OptionForge
storage/schema.py
--------------------------------------------------------------
OptionForge Standard Option Chain Schema
==============================================================
"""

from __future__ import annotations


class OptionChainSchema:
    """
    Standard OptionForge Option Chain Schema.

    Every data source (CSV, NSE, Broker API, Database)
    should be converted into this schema before entering
    the analytics engine.
    """

    # ==========================================================
    # Required Columns
    # ==========================================================

    REQUIRED_COLUMNS = [

        "SYMBOL",

        "EXPIRY",

        "STRIKE",

        "OPTION_TYPE",

        "LTP",

        "IV",

        "OI",

        "CHANGE_IN_OI",

        "VOLUME",

        "SPOT",

    ]

    # ==========================================================
    # Optional Columns
    # ==========================================================

    OPTIONAL_COLUMNS = [

        "OPEN",

        "HIGH",

        "LOW",

        "CLOSE",

        "BID",

        "ASK",

        "TIMESTAMP",

    ]

    # ==========================================================
    # Complete Schema
    # ==========================================================

    ALL_COLUMNS = REQUIRED_COLUMNS + OPTIONAL_COLUMNS

    # ==========================================================
    # Validation
    # ==========================================================

    @classmethod
    def validate(cls, columns: list[str]) -> tuple[bool, list[str]]:
        """
        Validate incoming column names.

        Returns
        -------
        (is_valid, missing_columns)
        """

        missing = [

            column

            for column in cls.REQUIRED_COLUMNS

            if column not in columns

        ]

        return len(missing) == 0, missing