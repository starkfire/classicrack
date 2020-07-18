from classicrack.utils.common import shift_mono, parse_text

class ROT13:
    """
    ROT13 is similar to Caesar Cipher, where each character takes a shift value of 13::

        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        NOPQRSTUVWXYZABCDEFGHIJKLM
    """

    def encode(self, text: str):
        """
        Encipher an input plaintext using ROT-13.

        :param text: input plaintext
        """
        return shift_mono(parse_text(text), 13)
    
    def decode(self, text: str):
        """
        Decipher an input ROT-13 ciphertext.

        :param text: input ciphertext
        """
        return shift_mono(parse_text(text), 13)