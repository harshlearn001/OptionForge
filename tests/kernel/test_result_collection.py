from optionforge.kernel.execution_result import ExecutionResult
from optionforge.kernel.execution_status import ExecutionStatus
from optionforge.kernel.result_collection import ResultCollection


def test_collection():

    results = ResultCollection(
        {
            "Dummy": ExecutionResult(
                engine="Dummy",
                status=ExecutionStatus.SUCCESS,
                result=100,
            )
        }
    )

    assert len(results) == 1
    assert results.exists("Dummy")
    assert results.get("Dummy").result == 100