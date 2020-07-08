from classicrack.utils.ngrams import *
import unittest

class TestNgrams(unittest.TestCase):

    def test_get_ngrams(self):
        target, n = 'cheemsburger', 2
        ngrams = get_ngrams(target, n)
        self.assertTrue(len(ngrams) == (len(target) - 1))

    def test_get_ngram_shifted_combinations(self):
        ngrams = get_ngram_shifted_combinations('th')
        self.assertTrue(len(ngrams) == 26)
    
    def test_common_bigrams(self):
        ngrams = common_bigrams('th')
        self.assertTrue(len(ngrams) == 26)
    
    def test_common_trigrams(self):
        ngrams = common_trigrams('the')
        self.assertTrue(len(ngrams) == 26)

if __name__ == '__main__':
    unittest.main()