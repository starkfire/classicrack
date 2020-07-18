from classicrack.utils.common import *
from classicrack.fitness.chi_squared import chi_squared
from classicrack.ngrams.monograms import monograms

class Affine:

    # check if slope is coprime with 26
    def coprime(self, slope: int):
        return is_coprime(slope, 26)

    # modular multiplicative inverse
    # will only be possible if slope is coprime with 26
    def get_inverse(self, slope: int):
        if not self.coprime(slope): raise ValueError('slope is not coprime with 26')
        for i in range(1, 26, 2):
            if (slope * i) % 26 == 1: return i

    def encode(self, text: str, slope: int, intercept: int):
        """
        Enciphers an input plaintext using Affine Cipher.
            text (str): input plaintext
            slope (int): slope value (must be coprime with 26)
            intercept (int): intercept value
        """
        if not self.coprime(slope): raise ValueError('slope is not coprime with 26')
        x = order_chars(parse_text(text))
        ct = [chr((slope * x[i] + intercept) % 26 + 97) for i in range(len(x))]
        return ''.join(str(x) for x in ct)
    
    def decode(self, text: str, slope: int, intercept: int):
        """
        Deciphers an input Affine ciphertext.
            text (str): input ciphertext
            slope (int): slope value (must be coprime with 26)
            intercept (int): intercept value
        """
        inv = self.get_inverse(slope)
        x = order_chars(parse_text(text))
        pt = [chr((inv * (x[i] - intercept)) % 26 + 97) for i in range(len(x))]
        return ''.join(str(x) for x in pt)
    
    def crack(self, text: str):
        """
        Cracks an input Affine ciphertext, and returns 
        plaintext values with acceptable fitness scores.
            text (str): input ciphertext
        """
        print("Cracking...\n")

        primes = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        ctxts = []
        for x in primes:
            for y in range(0, 26):
                ctxts.append(self.decode(text, x, y))
        results = chi_squared(ctxts, monograms)
        sorted_results = sorted(results.items(), key=lambda x: x[1])

        # show top 5 results
        print("CHI-SQUARE TEST (Top 5)")
        print("=======================")
        for x in range(5):
            print(str(round(sorted_results[x][1], 5)) + ': ' + str(sorted_results[x][0]) + '\n')
        
        return "Done."