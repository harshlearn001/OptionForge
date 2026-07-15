from dataclasses import dataclass


@dataclass(slots=True)
class ProviderMetric:

    provider: str

    duration_ms: float

    feature_count: int

    success: bool
