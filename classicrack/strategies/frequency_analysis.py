from classicrack.utils.common import *
from classicrack.utils.ngrams import *

def use_unigram(text: str):
    """
    Cracks an input ciphertext by taking its most frequent letter, and its distance to letter 'e',
    which is the most frequently used letter in the english alphabet.
        text (str): ciphertext
    """
    text = text.lower().replace(' ', '')
    most_frequent = most_frequent_char(text)
    shift = distance(most_frequent['char'], 'e')
    return shift_constant(text, shift)

def use_bigram(text: str):
    """
    Cracks an input ciphertext by taking its bigrams and checking for shifted combinations of the bigram 'th'.
        text (str): ciphertext
    """
    text = text.lower().replace(' ', '')
    ngrams = get_ngrams(text, 2)
    bigrams = common_bigrams()
    match = list(set(ngrams).intersection(bigrams))

    if (len(match) != 0):
        return [shift_constant(text, distance(match[x][0], 't'), decode=True) for x in range(len(match))]
    else:
        return None

def use_trigram(text: str):
    """
    Cracks an input ciphertext by taking its trigrams and checking for shifted combinations of the trigram 'the'.
        text (str): ciphertext
    """
    text = text.lower().replace(' ', '')
    ngrams = get_ngrams(text, 3)
    trigrams = common_trigrams()
    match = list(set(ngrams).intersection(trigrams))

    if (len(match) != 0):
        return [shift_constant(text, distance(match[x][2], 'e'), decode=True) for x in range(len(match))]
    else:
        return None