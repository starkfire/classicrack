from classicrack.utils.common import shift_mono

from classicrack.ngrams.monograms import monograms
from classicrack.fitness.chi_squared import chi_squared

class Caesar:
    """
    Caesar Cipher is a monoalphabetic substitution cipher where
    characters are shifted with a fixed shift value of ``n mod 26``.
    """

    def encode(self, text: str, shift: int):
        """
        Enciphers an input plaintext using Caesar.
        
        :param text: input plaintext
        :param shift: shift value
        """
        return shift_mono(parse_text(text), shift)
    
    def decode(self, text: str, shift: int):
        """
        Deciphers an input Caesar ciphertext.
        
        :param text: input ciphertext
        :param shift: shift value
        """
        return shift_mono(parse_text(text), shift, decode=True)

    def crack(self, text: str):
        """
        Cracks an input Caesar ciphertext and returns 
        plaintext values with acceptable fitness scores.
        
        :param text: input plaintext
        """
        print("Cracking...\n")
        ctxts = [shift_mono(text, x, decode=True) for x in range(26)]
        results = chi_squared(ctxts, monograms)
        sorted_results = sorted(results.items(), key=lambda x: x[1])

        print("CHI-SQUARE TEST (Top 5)")
        print("=======================")
        for x in range(5):
            print(str(round(sorted_results[x][1], 5)) + ': ' + str(sorted_results[x][0]) + '\n')
        
        return "Done."