"""
============================================================
OptionForge
Evidence Collection
============================================================

Author      : OptionForge
Module      : evidence_collection.py
Purpose     : Immutable collection of Evidence objects.

============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator

from optionforge.evidence.evidence import Evidence
from optionforge.evidence.evidence_direction import EvidenceDirection
from optionforge.evidence.evidence_level import EvidenceLevel
from optionforge.evidence.evidence_source import EvidenceSource


@dataclass(
    frozen=True,
    slots=True,
)
class EvidenceCollection:
    """
    Immutable collection of Evidence.
    """

    evidence: tuple[Evidence, ...] = field(
        default_factory=tuple,
    )

    # -----------------------------------------------------

    def __len__(self) -> int:

        return len(self.evidence)

    # -----------------------------------------------------

    def __iter__(self) -> Iterator[Evidence]:

        return iter(self.evidence)

    # -----------------------------------------------------

    def __getitem__(
        self,
        index: int,
    ) -> Evidence:

        return self.evidence[index]

    # -----------------------------------------------------

    def add(
        self,
        item: Evidence,
    ) -> "EvidenceCollection":
        """
        Return a new collection with one additional Evidence.
        """

        return EvidenceCollection(
            self.evidence + (item,),
        )

    # -----------------------------------------------------

    def by_source(
        self,
        source: EvidenceSource,
    ) -> "EvidenceCollection":

        return EvidenceCollection(
            tuple(
                e
                for e in self.evidence
                if e.source is source
            )
        )

    # -----------------------------------------------------

    def by_level(
        self,
        level: EvidenceLevel,
    ) -> "EvidenceCollection":

        return EvidenceCollection(
            tuple(
                e
                for e in self.evidence
                if e.level is level
            )
        )

    # -----------------------------------------------------

    def by_direction(
        self,
        direction: EvidenceDirection,
    ) -> "EvidenceCollection":

        return EvidenceCollection(
            tuple(
                e
                for e in self.evidence
                if e.direction is direction
            )
        )

    # -----------------------------------------------------

    @property
    def bullish(self) -> "EvidenceCollection":

        return EvidenceCollection(
            tuple(
                e
                for e in self.evidence
                if e.is_bullish
            )
        )

    # -----------------------------------------------------

    @property
    def bearish(self) -> "EvidenceCollection":

        return EvidenceCollection(
            tuple(
                e
                for e in self.evidence
                if e.is_bearish
            )
        )

    # -----------------------------------------------------

    @property
    def neutral(self) -> "EvidenceCollection":

        return EvidenceCollection(
            tuple(
                e
                for e in self.evidence
                if e.is_neutral
            )
        )

    # -----------------------------------------------------

    @property
    def strong(self) -> "EvidenceCollection":

        return EvidenceCollection(
            tuple(
                e
                for e in self.evidence
                if e.level.is_strong
            )
        )

    # -----------------------------------------------------

    @property
    def weak(self) -> "EvidenceCollection":

        return EvidenceCollection(
            tuple(
                e
                for e in self.evidence
                if e.level.is_weak
            )
        )

    # -----------------------------------------------------

    @property
    def sources(
        self,
    ) -> tuple[EvidenceSource, ...]:

        return tuple(
            sorted(
                {
                    e.source
                    for e in self.evidence
                },
                key=str,
            )
        )

    # -----------------------------------------------------

    def __repr__(self):

        return (
            f"EvidenceCollection("
            f"{len(self)} evidence)"
        )

    __str__ = __repr__