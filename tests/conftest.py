"""
============================================================
OptionForge
Pytest Configuration
============================================================

Author      : OptionForge
Module      : conftest.py

Purpose
-------
Shared pytest configuration.

Keep this file lightweight.

Use it for:
- Common pytest configuration
- Global fixtures (when truly shared)
- Session-level resources

Complex object builders should live in
tests/builders.py instead.

============================================================
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# ==========================================================
# Project Root
# ==========================================================

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


# ==========================================================
# Session Constants
# ==========================================================

@pytest.fixture(scope="session")
def total_capital() -> float:
    """
    Default portfolio capital.
    """
    return 100000.0


@pytest.fixture(scope="session")
def allocated_capital() -> float:
    """
    Default allocated capital.
    """
    return 40000.0


@pytest.fixture(scope="session")
def available_capital() -> float:
    """
    Default remaining capital.
    """
    return 60000.0


# ==========================================================
# Pytest Configuration
# ==========================================================

def pytest_configure(config):

    config.addinivalue_line(
        "markers",
        "slow: marks slow-running tests",
    )

    config.addinivalue_line(
        "markers",
        "integration: marks integration tests",
    )

    config.addinivalue_line(
        "markers",
        "unit: marks unit tests",
    )