from classicrack.ciphers import Caesar
import unittest

class TestCaesar(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(Caesar().encode('cheemsburmger', 13), 'purrzfoheztre')
    
    def test_decode(self):
        self.assertEqual(Caesar().decode('purrzfoheztre', 13), 'cheemsburmger')
    
    # method for checking instances of 'target' on the result list
    def check_matching_instances(self, result: list, target: str) -> bool:
        for x in range(len(result)):
            if (result[x] == target): return True
        return False
    
    # method for testing n-gram cracking
    def ngram_test(self, n):
        ciphertext = 'gurdhvpxoebjasbkwhzcfbiregurynmlqbt'
        target = 'thequickbrownfoxjumpsoverthelazydog'
        result = Caesar().crack_ngram(ciphertext, n)
        return self.check_matching_instances(result, target)
    
    def test_crack_bruteforce(self):
        result = Caesar().crack_bruteforce('purrzfoheztre')
        self.assertTrue(self.check_matching_instances(result, 'cheemsburmger'))
    
    def test_crack_unigram(self, n = 1):
        self.assertEqual(Caesar().crack_ngram('purrzfoheztre', 1), 'cheemsburmger')

    def test_crack_bigram(self, n = 2):
        self.assertTrue(self.ngram_test(2))
    
    def test_crack_trigram(self, n = 3):
        self.assertTrue(self.ngram_test(3))

if __name__ == '__main__':
    unittest.main()