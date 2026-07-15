from __future__ import annotations

from collections.abc import Iterator

from optionforge.kernel.engine import Engine


class Registry:

    def __init__(self):

        self._engines: dict[str, Engine] = {}

    def register(
        self,
        engine: Engine,
    ) -> None:

        self._engines[engine.name] = engine

    def get(
        self,
        name: str,
    ) -> Engine:

        return self._engines[name]

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._engines

    def values(self):

        return self._engines.values()

    def names(self):

        return tuple(self._engines.keys())

    def clear(self):

        self._engines.clear()

    def __iter__(self) -> Iterator[Engine]:

        return iter(self._engines.values())

    def __len__(self):

        return len(self._engines)
