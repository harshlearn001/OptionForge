"""
============================================================
OptionForge
WalkForwardRunner Tests
============================================================
"""

import pytest

from optionforge.research.walk_forward import (
    WalkForwardAnalysis,
)
from optionforge.research.walk_forward_runner import (
    WalkForwardRunner,
)


def runner():

    return WalkForwardRunner()


# ==========================================================
# Construction
# ==========================================================


def test_create():

    assert isinstance(
        runner(),
        WalkForwardRunner,
    )


# ==========================================================
# Empty Input
# ==========================================================


def test_empty():

    with pytest.raises(ValueError):

        runner().run([])


# ==========================================================
# Single Success
# ==========================================================


def test_single_success():

    result = runner().run(
        [True],
    )

    assert result.windows == 1

    assert result.successful_windows == 1

    assert result.failed_windows == 0

    assert result.success_rate == 100.0

    assert result.passed


# ==========================================================
# Single Failure
# ==========================================================


def test_single_failure():

    result = runner().run(
        [False],
    )

    assert result.windows == 1

    assert result.successful_windows == 0

    assert result.failed_windows == 1

    assert result.success_rate == 0.0

    assert not result.passed


# ==========================================================
# Mixed Results
# ==========================================================


def test_mixed():

    result = runner().run(
        [
            True,
            True,
            False,
            True,
        ]
    )

    assert result.windows == 4

    assert result.successful_windows == 3

    assert result.failed_windows == 1

    assert result.success_rate == 75.0

    assert result.stability_score == 75.0

    assert result.passed


# ==========================================================
# Multiple Failures
# ==========================================================


def test_multiple_failures():

    result = runner().run(
        [
            False,
            False,
            True,
            False,
        ]
    )

    assert result.successful_windows == 1

    assert result.failed_windows == 3

    assert result.success_rate == 25.0

    assert not result.passed


# ==========================================================
# Return Type
# ==========================================================


def test_result_type():

    result = runner().run(
        [
            True,
            False,
        ]
    )

    assert isinstance(
        result,
        WalkForwardAnalysis,
    )


# ==========================================================
# Stability
# ==========================================================


def test_stability():

    result = runner().run(
        [
            True,
            True,
            True,
            False,
            True,
        ]
    )

    assert result.stability_score == 80.0


# ==========================================================
# Representation
# ==========================================================


def test_repr():

    assert "WalkForwardRunner" in repr(
        runner(),
    )


def test_str():

    assert "WalkForwardRunner" in str(
        runner(),
    )
