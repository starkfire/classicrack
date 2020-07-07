from classicrack.utils.common import shift_constant

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