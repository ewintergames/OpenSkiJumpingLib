import unittest
from typing import List
from osj.jump_data import HillInfo, JumpData, JumpResult
from osj.result import FisResultsLoader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.lahti_130 = HillInfo.create(k=116, hs=130, gate_pts=7.56, head_wind=9.90, tail_wind=14.85,
                                         gates_spacing=0.65)

        self.jump_data = JumpData(distance=136.5, judges_points=[19, 19, 19.5, 19, 19.5], wind=1.35, gate=15)
        self.jump_result = JumpResult.create(self.jump_data, self.lahti_130, 16)

    def test_large_hill(self):
        self.assertEqual(self.lahti_130.k_points, 60)
        self.assertEqual(self.lahti_130.meter_points, 1.8)

    def test_jump_result(self):
        self.assertEqual(self.jump_result.style_points, 57.5)
        self.assertEqual(self.jump_result.distance_points, 96.9)
        self.assertEqual(self.jump_result.gate_points, 4.9)
        self.assertEqual(self.jump_result.wind_points, -13.4)


if __name__ == '__main__':
    unittest.main()
