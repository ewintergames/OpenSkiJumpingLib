from typing import List
from jump_data import JumpResult


class JumpResults:
    results = List[JumpResult]


class Result:
    results: JumpResults
    total_results: List[float]
    bibs: List[int]
    ranks: List[int]
    total_points: float

    def add_jump_result(self, result: JumpResult):
        self.results.results.append(self, result)