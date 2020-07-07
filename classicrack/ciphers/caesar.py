from classicrack.utils.common import *
from classicrack.utils.ngrams import *

from classicrack.strategies import frequency_analysis as fa

class Caesar:
    """
    Caesar Cipher Implementation.
    >>> cs = Caesar()
    >>> cs.encode('purrzfoheztre')
    """

    def encode(self, text: str, shift: int):
        return shift_constant(text.lower().replace(' ', ''), shift)
    
    def decode(self, text: str, shift: int):
        return shift_constant(text.lower().replace(' ', ''), shift, decode=True)

    def crack_bruteforce(self, text: str):
        values = [shift_constant(text, x, decode=True) for x in range(26)]
        return values
    
    def crack_ngram(self, text: str, n: int = 1):
        # TODO: function will sometimes return the correct value shifted one step backwards when n > 1
        text = text.lower().replace(' ', '')

        fa_strategy = {
            1: fa.use_unigram(text),
            2: fa.use_bigram(text),
            3: fa.use_trigram(text),
        }

        return fa_strategy.get(n, 'Invalid or unsupported n-value')