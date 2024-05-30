import unittest

from src.beers import find_min_beers_types


class TestFindMinBeersTypes(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(find_min_beers_types(3, 3, "NNYYNNYYY"), [0, 2])
        self.assertEqual(find_min_beers_types(2, 2, "YYNY"), [1])
        self.assertEqual(find_min_beers_types(2, 2, "YNNY"), [0, 1])
        self.assertEqual(find_min_beers_types(2, 2, "YNYN"), [0])
        self.assertEqual(find_min_beers_types(2, 2, "NYYY"), [1])

    def test_invalid_workers(self):
        self.assertEqual(find_min_beers_types(-1, 3, "NNYYNNYYY"), 'INCORRECT INPUT')
        self.assertEqual(find_min_beers_types(0, 3, "NNYYNNYYY"), 'INCORRECT INPUT')
        self.assertEqual(find_min_beers_types(50, 3, "NNYYNNYYY"), 'INCORRECT INPUT')

    def test_invalid_beer_types(self):
        self.assertEqual(find_min_beers_types(3, -1, "NNYYNNYYY"), 'INCORRECT INPUT')
        self.assertEqual(find_min_beers_types(3, 0, "NNYYNNYYY"), 'INCORRECT INPUT')
        self.assertEqual(find_min_beers_types(3, 50, "NNYYNNYYY"), 'INCORRECT INPUT')

    def test_incorrect_input_length(self):
        self.assertEqual(find_min_beers_types(3, 3, "NNYYNNYY"), 'INCORRECT INPUT')

    def test_no_Y_in_prefs(self):
        self.assertEqual(find_min_beers_types(3, 3, "NNNNNNNNN"), 'INCORRECT INPUT')

    def test_no_fulfilling_option(self):
        self.assertEqual(find_min_beers_types(3, 3, "NNNYNNNNN"),
                         'No condition fulfilling option is found. Most likely someone doesn\'t like any beer')

    def test_edge_cases(self):
        self.assertEqual(find_min_beers_types(1, 1, "Y"), [0])
        self.assertEqual(find_min_beers_types(49, 1, "Y"*49), [0])


if __name__ == '__main__':
    unittest.main()
