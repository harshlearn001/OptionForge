from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterator, Mapping


@dataclass(
    frozen=True,
    slots=True,
)
class Collection:
    """
    Immutable key-value collection.
    """

    values: Mapping[str, Any] = field(default_factory=dict)

    def get(self, name: str, default: Any = None) -> Any:
        return self.values.get(name, default)

    def keys(self):
        return self.values.keys()

    def values_view(self):
        return self.values.values()

    def items(self):
        return self.values.items()

    def __contains__(self, key: str) -> bool:
        return key in self.values

    def __len__(self):
        return len(self.values)

    def __iter__(self) -> Iterator[str]:
        return iter(self.values)