from enum import Enum


class JumpResultState(Enum):
    NoneState = 0
    Advanced = 1
    KoLoser = 2


class Gender(Enum):
    Male = 0
    Female = 1


class LimitType(Enum):
    WithoutLimit = 0
    Normal = 1
    Exact = 2


class RoundType(Enum):
    Normal = 0
    KO = 1
    Cup = 2
    CupLosers = 3


class ClassificationType(Enum):
    Place = 0
    Points = 1


class RankType(Enum):
    WithoutType = 0
    Event = 1
    Classification = 2


class OrdRankType(Enum):
    StartList = 0
    LastRound = 1
    LastRoundSeed = 2
    SameAsLastRound = 3
