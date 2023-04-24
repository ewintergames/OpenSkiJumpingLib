import json
from typing import List
from osj.jump_data import JumpResult


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


class ResultsLoader:
    @staticmethod
    def get_results_from_json(path: str):
        with open(path, "r") as json_file:
            print(json.loads(json_file))