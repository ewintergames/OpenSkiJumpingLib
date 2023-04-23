from typing import List
from jump_data import JumpResult


class JumpResults:
    results = List[JumpResult]


class Result:
    results: JumpResults
    qualRankPoints: float
    totalResults: List[float]
    bibs: List[int]
    rank: int
    totalPoints: float
