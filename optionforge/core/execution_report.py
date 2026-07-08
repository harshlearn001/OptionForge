from dataclasses import dataclass, field

from optionforge.core.metrics import ProviderMetric


@dataclass
class ExecutionReport:

    providers: list[ProviderMetric] = field(default_factory=list)

    def total_duration(self) -> float:

        return sum(p.duration_ms for p in self.providers)

    def total_features(self) -> int:

        return sum(p.feature_count for p in self.providers)

    def failures(self) -> int:

        return sum(not p.success for p in self.providers)