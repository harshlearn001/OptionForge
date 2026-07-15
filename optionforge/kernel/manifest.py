from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class EngineManifest:

    name: str

    version: str

    category: str

    author: str

    description: str

    result: str
