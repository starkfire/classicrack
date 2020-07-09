from classicrack.ciphers import Affine
import unittest

class TestAffine(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(Affine().encode('cheems burger', 5, 8), 'srccqunepmcp')
    
    def test_decode(self):
        self.assertEqual(Affine().decode('srccqunepmcp', 5, 8), 'cheemsburger')

if __name__ == '__main__':
    unittest.main()