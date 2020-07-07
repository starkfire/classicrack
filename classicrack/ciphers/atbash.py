class Atbash:

    def encode(self, text: str):
        """
        Encode an input text using Atbash.
            text (str): input text
        """
        text = text.lower().replace(' ', '')
        out = [chr(122 - ord(text[i]) + 97) for i in range(len(text))]
        return ''.join(str(x) for x in out)
    
    def decode(self, text: str):
        """
        Decode an input text using Atbash.
            text (str): input text
        """
        text = text.lower().replace(' ', '')
        out = [chr(122 - ord(text[i]) + 97) for i in range(len(text))]
        return ''.join(str(x) for x in out)