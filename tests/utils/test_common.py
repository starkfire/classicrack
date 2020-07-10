from classicrack.utils.common import *
import unittest

class TestCommon(unittest.TestCase):

    def test_parse_text(self):
        self.assertEqual(parse_text('cheems burger'), 'cheemsburger')
    
    def test_distance(self):
        dist = distance('j', 'e')
        self.assertEqual(dist, 5)

    def test_frequency(self):
        freq = frequency('the quick brown fox jumps over the lazy dog')
        most_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        self.assertEqual(most_freq[0][0], 'o')

    def test_shift_mono(self):
        self.assertEqual(shift_mono('cheems burger', 2), 'ejggoudwtigt')
        self.assertEqual(shift_mono('ejggoudwtigt', 2, decode=True), 'cheemsburger')
    
    def test_order_chars(self):
        self.assertEqual(order_chars('abcdefh'), [0, 1, 2, 3, 4, 5, 7])

if __name__ == '__main__':
    unittest.main()