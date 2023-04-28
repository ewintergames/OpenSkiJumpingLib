import numbers

from competition_enums import *
from osj.jump_data import JumpData
from osj.result import Result
from datetime import date
from typing import List


class Competitor:
    id_: str
    last_name: str
    first_name: str
    country_code: str
    club: str
    gender: Gender
    birth_date: date

    def __init__(self, id_: str, last_name: str, first_name: str, country_code: str, club: str, gender: Gender,
                 birth_date: date):
        self.birth_date = birth_date
        self.gender = gender
        self.club = club
        self.country_code = country_code
        self.first_name = first_name
        self.last_name = last_name
        self.id_ = id_


class RoundInfo:
    round_type: RoundType
    out_limit_type: LimitType
    out_limit: int
    use_ord_rank: OrdRankType
    reversed_bibs: bool

    def __int__(self, round_type: RoundType, out_limit_type: LimitType, out_limit: int, use_ord_rank: OrdRankType,
                reversed_bibs: bool):
        self.round_type = round_type
        self.out_limit_type = out_limit_type
        self.out_limit = out_limit
        self.use_ord_rank = use_ord_rank
        self.reversed_bibs = reversed_bibs


class EventInfo:
    id: int
    hill_id: str
    classifications: List[int]
    round_infos: List[RoundInfo]


class EventResults:
    competitor_ids: List[int]
    results: List[Result]
    final_results: List[int]
    all_round_results: List[int]
