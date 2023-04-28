from dataclasses import dataclass
from typing import List, Tuple, Self
from competition.competition_enums import JumpResultState


@dataclass
class HillInfo:
    k: float
    hs: float
    gates_spacing: float
    gate_points: float
    tail_wind_points: float
    head_wind_points: float
    k_points: float
    meter_points: float

    @classmethod
    def create(cls, k: float, hs: float, tail_wind: float, head_wind: float, gate_pts: float,
               gates_spacing: float) -> Self:
        points_table: List[Tuple[float, float]] = [
            (0, 4.8),
            (25, 4.4),
            (30, 4.0),
            (35, 3.6),
            (40, 3.2),
            (50, 2.8),
            (60, 2.4),
            (70, 2.2),
            (80, 2.0),
            (100, 1.8),
            (170, 1.2)]
        k_point_pts = 120 if k >= 170 else 60
        points_per_meter = 0
        for kk, pts in points_table:
            if k >= kk:
                points_per_meter = pts

        return cls(k=k, hs=hs, gates_spacing=gates_spacing, gate_points=gate_pts, tail_wind_points=tail_wind,
                   head_wind_points=head_wind, k_points=k_point_pts, meter_points=points_per_meter)


@dataclass
class JumpData:
    distance: float
    judges_points: List[float]
    gate: int
    wind: float


@dataclass
class JumpResult:
    distance: float
    distance_points: float
    judges: List[Tuple[float, bool]]
    style_points: float
    gates_diff: int
    gate_points: float
    wind: float
    wind_points: float
    state: JumpResultState = JumpResultState.NoneState

    @classmethod
    def create(cls, jump_data: JumpData, hill_info: HillInfo, gate_on_round_start: int, jump_state = JumpResultState) -> Self:
        min_ind = min((v, i) for i, v in enumerate(jump_data.judges_points))[0]
        max_ind = max((v, i) for i, v in enumerate(jump_data.judges_points))[0]
        judges = [(val, i != min_ind and i != max_ind) for i, val in enumerate(jump_data.judges_points)]
        diff = gate_on_round_start - jump_data.gate
        return cls(
            distance=jump_data.distance,
            distance_points=hill_info.k_points + (jump_data.distance - hill_info.k) * hill_info.meter_points,
            judges=judges,
            style_points=sum(val for val, flag in judges if flag) - min_ind - max_ind,
            gates_diff= diff,
            gate_points= round(diff * hill_info.gates_spacing * hill_info.gate_points, 1),
            wind=jump_data.wind,
            wind_points=round(jump_data.wind * (
                -hill_info.head_wind_points if jump_data.wind > 0 else hill_info.tail_wind_points), 1),
            state=jump_state
        )
