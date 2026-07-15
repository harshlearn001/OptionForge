"""
============================================================
OptionForge
RiskResult Tests
============================================================
"""

from optionforge.risk.risk_result import RiskResult
from optionforge.risk.rule_result import RuleResult


def passed_rule(
    score: float = 5.0,
) -> RuleResult:

    return RuleResult(
        rule_name="CapitalRule",
        score=score,
        passed=True,
        warnings=(),
        reasons=("Rule passed.",),
    )


def failed_rule(
    score: float = 80.0,
) -> RuleResult:

    return RuleResult(
        rule_name="MarginRule",
        score=score,
        passed=False,
        warnings=("Margin exceeded.",),
        reasons=("Margin policy failed.",),
    )


def test_empty_result():

    result = RiskResult()

    assert result.rule_count == 0

    assert result.overall_score == 0.0

    assert result.passed

    assert result.warning_count == 0

    assert result.reason_count == 0


def test_rule_count():

    result = RiskResult(
        rule_results=(
            passed_rule(),
            failed_rule(),
        ),
    )

    assert result.rule_count == 2


def test_average_score():

    result = RiskResult(
        rule_results=(
            passed_rule(
                score=10.0,
            ),
            failed_rule(
                score=30.0,
            ),
        ),
    )

    assert result.overall_score == 20.0


def test_passed_false():

    result = RiskResult(
        rule_results=(
            passed_rule(),
            failed_rule(),
        ),
    )

    assert not result.passed


def test_passed_true():

    result = RiskResult(
        rule_results=(
            passed_rule(),
            passed_rule(),
        ),
    )

    assert result.passed


def test_warning_collection():

    result = RiskResult(
        rule_results=(
            passed_rule(),
            failed_rule(),
        ),
    )

    assert result.warning_count == 1

    assert "Margin exceeded." in result.warnings


def test_reason_collection():

    result = RiskResult(
        rule_results=(
            passed_rule(),
            failed_rule(),
        ),
    )

    assert result.reason_count == 2


def test_to_dict():

    result = RiskResult(
        rule_results=(passed_rule(),),
    )

    data = result.to_dict()

    assert data["rule_count"] == 1

    assert data["passed"] is True


def test_str():

    result = RiskResult(
        rule_results=(passed_rule(),),
    )

    assert "RiskResult" in str(result)


def test_repr():

    result = RiskResult(
        rule_results=(passed_rule(),),
    )

    assert "RiskResult" in repr(result)
