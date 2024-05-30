import unittest
import math
from src.wires import calculate_max_wire_length


class TestCalculateMaxWireLength(unittest.TestCase):

    def test_example_case(self):
        w = 2
        heights = [3, 3, 3]
        expected_length = round(math.sqrt(2 ** 2 + 2 ** 2) * 2, 2)  # 2 * sqrt(8) = 2 * 2.828427 = 5.656854
        result = round(calculate_max_wire_length(w, heights), 2)
        self.assertEqual(result, expected_length)

    def test_single_pole(self):
        w = 1
        heights = [5]
        expected_length = 0.00
        result = calculate_max_wire_length(w, heights)
        self.assertEqual(result, expected_length)

    def test_two_poles(self):
        w = 4
        heights = [1, 10]
        expected_length = round(math.sqrt(4 ** 2 + 9 ** 2), 2)  # sqrt(16 + 81) = sqrt(97) = 9.85
        result = round(calculate_max_wire_length(w, heights), 2)
        self.assertEqual(result, expected_length)

    def test_invalid_w(self):
        with self.assertRaises(ValueError) as context:
            calculate_max_wire_length(0, [3, 3, 3])
        self.assertTrue("Відстань між опорами має бути у діапазоні від 1 до 100." in str(context.exception))

    def test_invalid_height(self):
        with self.assertRaises(ValueError) as context:
            calculate_max_wire_length(2, [3, 0, 3])
        self.assertTrue("Висота кожної опори має бути у діапазоні від 1 до 100." in str(context.exception))

    def test_long_input(self):
        w = 4
        heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70,
             75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        expected_length = 2738.18
        result = round(calculate_max_wire_length(w, heights), 2)
        self.assertEqual(result, expected_length)


if __name__ == '__main__':
    unittest.main()
