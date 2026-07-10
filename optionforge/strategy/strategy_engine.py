"""
============================================================
OptionForge
Strategy Engine
============================================================

Author      : OptionForge
Module      : strategy_engine.py

Purpose
-------
Institutional orchestration engine for Strategy.

Pipeline

    Decision
        ↓
    StrategyBuilder
        ↓
    Strategy
        ↓
    ExecutionPlanBuilder
        ↓
    ExecutionPlan
        ↓
    StrategyResult

Contains NO business logic.

============================================================
"""

from __future__ import annotations

from optionforge.decision.decision import (
    Decision,
)

from optionforge.strategy.execution_plan_builder import (
    ExecutionPlanBuilder,
)
from optionforge.strategy.risk_profile import (
    RiskProfile,
)
from optionforge.strategy.strategy_builder import (
    StrategyBuilder,
)
from optionforge.strategy.strategy_result import (
    StrategyResult,
)
from optionforge.strategy.strategy_selector import (
    StrategySelector,
)


class StrategyEngine:
    """
    Institutional Strategy Engine.

    Orchestrates construction of the complete
    StrategyResult.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(
        self,
        *,
        risk_profile: RiskProfile = RiskProfile.MODERATE,
        selector: StrategySelector | None = None,
        strategy_builder: StrategyBuilder | None = None,
        execution_plan_builder: (
            ExecutionPlanBuilder | None
        ) = None,
    ) -> None:

        self._selector = (

            selector

            if selector is not None

            else StrategySelector(

                risk_profile=risk_profile,

            )

        )

        self._strategy_builder = (

            strategy_builder

            if strategy_builder is not None

            else StrategyBuilder(

                selector=self._selector,

            )

        )

        self._execution_plan_builder = (

            execution_plan_builder

            if execution_plan_builder is not None

            else ExecutionPlanBuilder()

        )

    # =====================================================
    # Public API
    # =====================================================

    def build(
        self,
        decision: Decision,
    ) -> StrategyResult:
        """
        Build the complete institutional
        StrategyResult.
        """

        strategy = self._strategy_builder.build(

            decision,

        )

        execution_plan = (

            self._execution_plan_builder.build(

                strategy,

            )

        )

        return StrategyResult(

            strategy=strategy,

            execution_plan=execution_plan,

            metadata={

                "engine": "StrategyEngine",

            },

        )

    # =====================================================
    # Callable
    # =====================================================

    def __call__(
        self,
        decision: Decision,
    ) -> StrategyResult:

        return self.build(

            decision,

        )

    # =====================================================
    # Convenience
    # =====================================================

    @property
    def selector(
        self,
    ) -> StrategySelector:

        return self._selector

    @property
    def strategy_builder(
        self,
    ) -> StrategyBuilder:

        return self._strategy_builder

    @property
    def execution_plan_builder(
        self,
    ) -> ExecutionPlanBuilder:

        return self._execution_plan_builder

    # =====================================================
    # Representation
    # =====================================================

    def __repr__(
        self,
    ) -> str:

        return (

            f"{self.__class__.__name__}("

            f"risk_profile="

            f"{self.selector.risk_profile.name})"

        )