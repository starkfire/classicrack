from classicrack.utils.common import parse_text

class Atbash:
    """
    Atbash implementation.
    >>> ab = Atbash()
    >>> ab.encode('zebras')
    >>> ab.decode('avyizh')
    """

    def encode(self, text: str):
        """
        Encode an input text using Atbash.
            text (str): input text
        """
        text = parse_text(text)
        out = [chr(122 - ord(text[i]) + 97) for i in range(len(text))]
        return ''.join(str(x) for x in out)
    
    def decode(self, text: str):
        """
        Decode an input text using Atbash.
            text (str): input text
        """
        text = parse_text(text)
        out = [chr(122 - ord(text[i]) + 97) for i in range(len(text))]
        return ''.join(str(x) for x in out)