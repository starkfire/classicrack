from classicrack.utils.common import *
from classicrack.utils.ngrams import *

def use_unigram(text: str, unigram: str = 'e'):
    """
    Cracks an input ciphertext based on a unigram (i.e. 'e').
        text (str): ciphertext
    """
    if (len(unigram) != 1): raise ValueError
    text = parse_text(text)
    sorted_freq = sorted(frequency(text).items(), key=lambda x: x[1], reverse=True)
    shift = distance(sorted_freq[0][0], unigram)
    return shift_mono(text, shift)

def use_bigram(text: str):
    """
    Cracks an input ciphertext by taking its bigrams and checking for shifted combinations of the bigram 'th'.
        text (str): ciphertext
    """
    match = find_ngram_equivalents(text, common_bigrams(), 2)

    if (len(match) != 0):
        return [shift_mono(text, distance(match[x][0], 't'), decode=True) for x in range(len(match))]
    else:
        return None

def use_trigram(text: str):
    """
    Cracks an input ciphertext by taking its trigrams and checking for shifted combinations of the trigram 'the'.
        text (str): ciphertext
    """
    match = find_ngram_equivalents(text, common_trigrams(), 3)

    if (len(match) != 0):
        return [shift_mono(text, distance(match[x][2], 'e'), decode=True) for x in range(len(match))]
    else:
        return None