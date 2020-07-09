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
        return shift_mono(parse_text(text), shift)
    
    def decode(self, text: str, shift: int):
        return shift_mono(parse_text(text), shift, decode=True)

    def crack_bruteforce(self, text: str):
        values = [shift_mono(text, x, decode=True) for x in range(26)]
        return values
    
    def crack_ngram(self, text: str, n: int = 1):
        text = parse_text(text)

        fa_strategy = {
            1: fa.use_unigram(text),
            2: fa.use_bigram(text),
            3: fa.use_trigram(text),
        }

        return fa_strategy.get(n, 'Invalid or unsupported n-value')