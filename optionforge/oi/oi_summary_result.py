from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class OISummaryResult:
    """
    Institutional Open Interest Summary.
    """

    call_oi: int
    put_oi: int
    total_oi: int

    call_volume: int
    put_volume: int
    total_volume: int

    call_share: float
    put_share: float

    pcr: float

    strikes: int

    dominant_side: str
