from classicrack.utils.common import *
from classicrack.utils.ngrams import *

def use_unigram(text: str):
    text = text.lower().replace(' ', '')
    most_frequent = most_frequent_char(text)
    shift = distance(most_frequent['char'], 'e')
    print(shift)
    return shift_constant(text, shift)

def use_bigram(text: str):
    text = text.lower().replace(' ', '')
    ngrams = get_ngrams(text, 2)
    bigrams = common_bigrams()
    match = get_common_ngrams(ngrams, bigrams)

    if (len(match) != 0):
        return shift_constant(text, distance(match[0][0], 't'), decode=True)
    else:
        return None

def use_trigram(text: str):
    text = text.lower().replace(' ', '')
    ngrams = get_ngrams(text, 3)
    trigrams = common_trigrams()
    match = get_common_ngrams(ngrams, trigrams)

    if (len(match) != 0):
        return shift_constant(text, distance(match[0][2], 'e'), decode=True)
    else:
        return None