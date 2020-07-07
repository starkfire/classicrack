from classicrack.utils.common import shift_constant

class ROT13:
    """
    ROT13 Implementation.
    >>> rot = ROT13()
    >>> rot.encode('cheemsburmger')
    >>> rot.decode('purrzfoheztre')
    """

    def encode(self, text: str):
        return shift_constant(text.lower().replace(' ', ''), 13)
    
    def decode(self, text: str):
        return shift_constant(text.lower().replace(' ', ''), 13)