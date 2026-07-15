from dataclasses import dataclass

from optionforge.kernel.collection import Collection


@dataclass(
    frozen=True,
    slots=True,
)
class AnalyticsCollection(Collection):
    """Analytics stage outputs."""
