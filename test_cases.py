import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):

    # 同値分割法
    def test_valid_case(self):
        self.assertEqual(calc(2, 5), 10)  # 有効な入力

    def test_invalid_case_out_of_range(self):
        self.assertEqual(calc(0, 1000), -1)  # 範囲外

    # 境界値分割法
    def test_boundary_case_within(self):
        self.assertEqual(calc(0.001, 999.999), 0.001 * 999.999)  # 境界内

    def test_boundary_case_outside(self):
        self.assertEqual(calc(0, 1000), -1)  # 境界外

    # 異常ケース
    def test_non_numeric_input(self):
        self.assertEqual(calc("abc", 5), -1)  # 非数値
        self.assertEqual(calc(None, 10), -1)  # None

    # 順序の確認
    def test_invalid_order(self):
        self.assertEqual(calc(10, 5), -1)  # A > B の場合

if __name__ == '__main__':
    unittest.main()
