# utility functions for common tasks

def distance(x: chr, y: chr = 'e'):
    """
    Get the distance between two characters in the alphabet
    """
    return (ord(x) - ord(y)) % 26

def most_frequent_char(txt: str):
    """
    Gets the most frequent character on a given text
    """
    txt = txt.lower().replace(' ', '')
    freq = {}
    
    for x in txt:
        freq[x] = (lambda: 1, lambda: freq[x] + 1)[x in freq]()
    
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    return { 'char': freq[0][0], 'freq': freq[0][1] }

def shift_constant(txt: str, shift: int, decode: bool = False):
    """
    Shifts all characters of an input text using a constant shift number.
    """
    txt = txt.lower().replace(' ', '')
    if (decode): shift = -shift
    out = [chr((ord(txt[i]) + shift - 97) % 26 + 97) for i in range(len(txt))]
    
    return ''.join(str(x) for x in out)