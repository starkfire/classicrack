from classicrack.utils.common import order_chars, parse_text, is_coprime

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
        if not self.coprime(slope): raise ValueError('slope is not coprime with 26')
        x = order_chars(parse_text(text))
        ct = [chr((slope * x[i] + intercept) % 26 + 97) for i in range(len(x))]
        return ''.join(str(x) for x in ct)
    
    def decode(self, text: str, slope: int, intercept: int):
        inv = self.get_inverse(slope)
        x = order_chars(parse_text(text))
        pt = [chr((inv * (x[i] - intercept)) % 26 + 97) for i in range(len(x))]
        return ''.join(str(x) for x in pt)