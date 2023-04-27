import json
import requests
from bs4 import BeautifulSoup

from typing import List
from osj.jump_data import JumpResult, JumpData


class JumpResults:
    results = List[JumpResult]


class Result:
    results: JumpResults
    total_results: List[float]
    bibs: List[int]
    ranks: List[int]
    total_points: float

    def add_jump_result(self, result: JumpResult):
        self.results.results.append(result)


class FisResultsLoader:
    base_row = [('rank', int), ('bib', int), ('name', str), ('country', str), ('total', float)]
    result_row = [('speed', float), ('distance', float), ('distance_points', float),
                  ('a', float), ('b', float), ('c', float), ('d', float), ('e', float), ('judges', float),
                  ('gate', int), ('gate_points', float), ('wind', float), ('wind_points', float),
                  ('total', float), ('rank', int)]

    @staticmethod
    def read_results_from_json(path: str):
        with open(path, "r") as json_file:
            return json.load(json_file)

    @staticmethod
    def get_result(item):
        subrows = item.select('.g-row.container > .g-row')
        subrows_split = map(lambda sr: sr.get_text().splitlines(), subrows)
        return [list(filter(lambda x: x != '', map(lambda x: x.strip(), sr))) for sr in subrows_split]

    @staticmethod
    def load_results_from_fis_site(race_id):
        url = 'https://data.fis-ski.com/fis_events/ajax/raceresultsfunctions/details.html'
        page = requests.get(url, params={'sectorcode': 'JP', 'raceid': race_id})
        soup = BeautifulSoup(page.content, 'html.parser')
        items = soup.select('#events-info-results a.table-row.table-row_theme_small')
        return [FisResultsLoader.get_result(item) for item in items]

    @staticmethod
    def get_result_dict(result):
        res_dict = {"jumps": [], 'diff': 0}
        for value, (name, cls) in zip(result[0], FisResultsLoader.base_row):
            res_dict[name] = cls(value)

        if len(result[1]) > 15:
            res_dict['diff'] = float(result[1][15])

        for jump in result[1:]:
            jump_dict = {}
            for value, (name, cls) in zip(jump, FisResultsLoader.result_row):
                jump_dict[name] = cls(value)
            res_dict['jumps'].append(jump_dict)

        return res_dict

    @staticmethod
    def get_jump_data_from_json(data):
        return JumpData(
            distance=data['distance'],
            judges_points=[data['A'], data['B'], data['C'], data['D'], data['E']],
            gate=data['gate'],
            wind=data['wind']
        )
