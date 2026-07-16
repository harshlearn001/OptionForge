from optionforge.kernel.execution_status import ExecutionStatus


def test_success():

    assert ExecutionStatus.SUCCESS.is_success
    assert not ExecutionStatus.SUCCESS.is_failed


def test_failed():

    assert ExecutionStatus.FAILED.is_failed
    assert not ExecutionStatus.FAILED.is_success


def test_warning():

    assert ExecutionStatus.WARNING.is_warning


def test_skipped():

    assert ExecutionStatus.SKIPPED.is_skipped