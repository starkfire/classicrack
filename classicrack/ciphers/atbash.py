from classicrack.utils.common import parse_text

class Atbash:
    """
    Atbash is a monoalphabetic substitution cipher that is similar to Affine Cipher.
    Unlike Affine, Atbash takes the following function for encryption and decryption::

        E(x) = D(x) = (-x mod m) + 1
    """

    def encode(self, text: str):
        """
        Encipher an input plaintext using Atbash.
        
        :param text: input plaintext
        """
        text = parse_text(text)
        out = [chr(122 - ord(text[i]) + 97) for i in range(len(text))]
        return ''.join(str(x) for x in out)
    
    def decode(self, text: str):
        """
        Decipher an input Atbash ciphertext.

        :param text: input ciphertext
        """
        text = parse_text(text)
        out = [chr(122 - ord(text[i]) + 97) for i in range(len(text))]
        return ''.join(str(x) for x in out)