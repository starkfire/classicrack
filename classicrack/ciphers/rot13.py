from classicrack.utils.common import shift_constant, parse_text

class ROT13:
    """
    ROT13 Implementation.
    >>> rot = ROT13()
    >>> rot.encode('cheemsburmger')
    >>> rot.decode('purrzfoheztre')
    """

    def encode(self, text: str):
        return shift_constant(parse_text(text), 13)
    
    def decode(self, text: str):
        return shift_constant(parse_text(text), 13)