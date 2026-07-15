"""
============================================================
OptionForge
Institutional Decision Rule
============================================================

Author      : OptionForge
Module      : institutional_decision_rule.py

Purpose
-------
Primary institutional decision rule.

This rule delegates decision construction to the
DecisionBuilder.

It contains no decision-construction logic.

============================================================
"""

from __future__ import annotations

from optionforge.decision.decision import (
    Decision,
)
from optionforge.decision.decision_builder import (
    DecisionBuilder,
)
from optionforge.decision.rules.decision_rule import (
    DecisionRule,
)
from optionforge.marketdna.market_dna import (
    MarketDNA,
)


class InstitutionalDecisionRule(DecisionRule):
    """
    Primary institutional decision rule.

    The rule evaluates MarketDNA and delegates the
    construction of the immutable Decision to the
    DecisionBuilder.
    """

    def evaluate(
        self,
        *,
        market_dna: MarketDNA,
        builder: DecisionBuilder,
    ) -> Decision | None:
        """
        Produce an institutional trading decision.

        Parameters
        ----------
        market_dna
            Immutable market state.

        builder
            DecisionBuilder responsible for creating
            the immutable Decision object.

        Returns
        -------
        Decision
            Institutional trading decision.
        """

        return builder.build(
            market_dna,
        )
