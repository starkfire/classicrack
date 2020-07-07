from classicrack.utils.ngrams import *
import unittest

class TestNgrams(unittest.TestCase):

    def test_get_ngrams(self):
        ngram_2 = ['ch', 'he', 'ee', 'em', 'ms', 'sb', 'bu', 'ur', 'rg', 'ge', 'er']
        ngrams = get_ngrams('cheems burger', 2)
        for i in range(len(ngrams)):
            self.assertEqual(ngrams[i], ngram_2[i])
    
    def test_shift_ngram(self):
        self.assertEqual(shift_ngram('th', 3), 'wk')

    def test_get_ngram_shifted_combinations(self):
        ngram_2 = ['th', 'ui', 'vj', 'wk', 'xl', 'ym', 'zn', 'ao', 'bp', 'cq', 'dr', 'es', 'ft', 'gu', 'hv', 'iw', 'jx', 'ky', 'lz', 'ma', 'nb', 'oc', 'pd', 'qe', 'rf', 'sg']
        ngrams = get_ngram_shifted_combinations('th')
        for i in range(len(ngrams)):
            self.assertEqual(ngrams[i], ngram_2[i])
    
    def test_common_bigrams(self):
        ngram_2 = ['th', 'ui', 'vj', 'wk', 'xl', 'ym', 'zn', 'ao', 'bp', 'cq', 'dr', 'es', 'ft', 'gu', 'hv', 'iw', 'jx', 'ky', 'lz', 'ma', 'nb', 'oc', 'pd', 'qe', 'rf', 'sg']
        ngrams = common_bigrams('th')
        for i in range(len(ngrams)):
            self.assertEqual(ngrams[i], ngram_2[i])
    
    def test_common_trigrams(self):
        ngram_3 = ['the', 'uif', 'vjg', 'wkh', 'xli', 'ymj', 'znk', 'aol', 'bpm', 'cqn', 'dro', 'esp', 'ftq', 'gur', 'hvs', 'iwt', 'jxu', 'kyv', 'lzw', 'max', 'nby', 'ocz', 'pda', 'qeb', 'rfc', 'sgd']
        ngrams = common_trigrams('the')
        for i in range(len(ngrams)):
            self.assertEqual(ngrams[i], ngram_3[i])

if __name__ == '__main__':
    unittest.main()