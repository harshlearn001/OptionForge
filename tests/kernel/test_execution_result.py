from optionforge.kernel.execution_result import ExecutionResult
from optionforge.kernel.execution_status import ExecutionStatus


def test_execution_result():

    result = ExecutionResult(
        engine="DummyEngine",
        status=ExecutionStatus.SUCCESS,
        result=123,
        duration=0.5,
    )

    assert result.engine == "DummyEngine"
    assert result.result == 123
    assert result.succeeded
    assert result.duration == 0.5