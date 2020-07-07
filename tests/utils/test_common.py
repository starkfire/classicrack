from classicrack.utils.common import *
import unittest

class TestCommon(unittest.TestCase):

    def test_distance(self):
        dist = distance('j', 'e')
        self.assertEqual(dist, 5)

    def test_get_most_frequent_char(self):
        most_frequent = most_frequent_char('the quick brown fox jumps over the lazy dog')
        self.assertEqual(most_frequent, { 'char': 'o', 'freq': 4 })

    def test_shift_constant(self):
        self.assertEqual(shift_constant('cheems burger', 2), 'ejggoudwtigt')
        self.assertEqual(shift_constant('ejggoudwtigt', 2, decode=True), 'cheemsburger')

if __name__ == '__main__':
    unittest.main()