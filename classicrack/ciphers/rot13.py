from classicrack.utils.common import shift_mono, parse_text

class ROT13:
    """
    ROT13 Implementation.
    >>> rot = ROT13()
    >>> rot.encode('cheemsburmger')
    >>> rot.decode('purrzfoheztre')
    """

    def encode(self, text: str):
        """
        Encipher an input plaintext using ROT-13.
        """
        return shift_mono(parse_text(text), 13)
    
    def decode(self, text: str):
        """
        Decipher an input ROT-13 ciphertext.
        """
        return shift_mono(parse_text(text), 13)