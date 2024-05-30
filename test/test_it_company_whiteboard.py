import unittest

from src.it_company_whiteboard import smallest_square_to_fit_rectangles

class TestSmallestSquareToFitRectangles(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(smallest_square_to_fit_rectangles(10, 2, 3), 8)
        self.assertEqual(smallest_square_to_fit_rectangles(11, 10, 1), 11)  # HE-HE
        self.assertEqual(smallest_square_to_fit_rectangles(5, 2, 2), 5)
        self.assertEqual(smallest_square_to_fit_rectangles(100, 5, 5), 50)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            smallest_square_to_fit_rectangles("10", 2, 3)
        with self.assertRaises(ValueError):
            smallest_square_to_fit_rectangles(10, -2, 3)
        with self.assertRaises(ValueError):
            smallest_square_to_fit_rectangles(0, 2, 3)
        with self.assertRaises(ValueError):
            smallest_square_to_fit_rectangles(10, 0, 3)
        with self.assertRaises(ValueError):
            smallest_square_to_fit_rectangles(10, 2, 0)


if __name__ == '__main__':
    unittest.main()
