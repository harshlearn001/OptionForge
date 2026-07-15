"""
============================================================
OptionForge
FillStatus Tests
============================================================
"""

from optionforge.execution.fill_status import FillStatus


def test_partial():

    assert FillStatus.PARTIAL.is_partial

    assert not FillStatus.PARTIAL.is_complete


def test_complete():

    assert FillStatus.COMPLETE.is_complete

    assert not FillStatus.COMPLETE.is_partial


def test_cancelled():

    assert FillStatus.CANCELLED.is_cancelled


def test_rejected():

    assert FillStatus.REJECTED.is_rejected


def test_str():

    assert str(FillStatus.PARTIAL) == "Partial"

    assert str(FillStatus.COMPLETE) == "Complete"
