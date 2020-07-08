from classicrack.ciphers import ROT13
import unittest

class TestROT13(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(ROT13().encode('cheemsburmger'), 'purrzfoheztre')
    
    def test_decode(self):
        self.assertEqual(ROT13().decode('purrzfoheztre'), 'cheemsburmger')

if __name__ == '__main__':
    unittest.main()