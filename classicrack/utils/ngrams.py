# utility functions for handling n-grams

from classicrack.utils.common import parse_text, shift_constant

def get_ngrams(text: str, n: int):
    """
    Returns a list of n-grams from an input text
        text (str): input text
        n (int): number of characters for each item
    """
    text = parse_text(text)
    return [text[i: i + n] for i in range(len(text) - n + 1)]

def get_ngram_shifted_combinations(ngram: str):
    """
    Takes an n-gram and shifts its characters for up to 26 steps
        ngram (str): input n-gram
    """
    ngrams = []
    for x in range(26):
        ngrams.append(shift_constant(ngram, x))
    return ngrams

def common_bigrams(bigram: str = 'th'):
    """
    Takes a bigram and returns its shifted combinations.
        bigram (str): an input bigram (e.g. 'th')
    """
    bigrams = get_ngram_shifted_combinations(bigram)
    return bigrams

def common_trigrams(trigram: str = 'the'):
    """
    Takes a trigram and returns its shifted combinations.
        trigram (str): an input trigram (e.g. 'the')
    """
    trigrams = get_ngram_shifted_combinations(trigram)
    return trigrams