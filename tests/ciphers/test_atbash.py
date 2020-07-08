from classicrack.ciphers import Atbash
import unittest

class TestAtbash(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(Atbash().encode('zebras'), 'avyizh')
    
    def test_decode(self):
        self.assertEqual(Atbash().decode('avyizh'), 'zebras')

if __name__ == '__main__':
    unittest.main()