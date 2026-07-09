from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Engine(ABC):
    """
    Base engine contract.
    """

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def version(self) -> str:
        return "1.0"

    @property
    def category(self) -> str:
        return "Unknown"

    @property
    def description(self) -> str:
        return ""

    @abstractmethod
    def execute(
        self,
        snapshot: Any,
    ) -> Any:
        ...