import unittest

from src.knuth_morris_pratt import build_prefix_table, kmp_search


class TestKMP(unittest.TestCase):

    def test_build_prefix_table(self):
        self.assertEqual(build_prefix_table("ABABACA"), [0, 0, 1, 2, 3, 0, 1])
        self.assertEqual(build_prefix_table("AAAA"), [0, 1, 2, 3])
        self.assertEqual(build_prefix_table("ABCDE"), [0, 0, 0, 0, 0])
        self.assertEqual(build_prefix_table("ANHOI"), [0, 0, 0, 0, 0])

    def test_kmp_search(self):
        self.assertEqual(kmp_search("ABABABABAC", "ABABAC"), [4])
        self.assertEqual(kmp_search("AAAAA", "AA"), [0, 1, 2, 3])
        self.assertEqual(kmp_search("ABCABCABC", "ABC"), [0, 3, 6])


if __name__ == '__main__':
    unittest.main()
