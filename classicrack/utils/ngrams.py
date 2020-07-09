# utility functions for handling n-grams

from classicrack.utils.common import parse_text, shift_mono

def get_ngrams(text: str, n: int):
    """
    Returns a list of n-grams from an input text
        text (str): input text
        n (int): number of characters for each item
    """
    return [text[i: i + n] for i in range(len(parse_text(text)) - n + 1)]

def get_ngram_shifted_combinations(ngram: str):
    """
    Takes an n-gram and shifts its characters for up to 26 steps
        ngram (str): input n-gram
    """
    return [shift_mono(ngram, x) for x in range(26)]

def common_bigrams(bigram: str = 'th'):
    """
    Takes a bigram and returns its shifted combinations.
        bigram (str): an input bigram (e.g. 'th')
    """
    return get_ngram_shifted_combinations(bigram)

def common_trigrams(trigram: str = 'the'):
    """
    Takes a trigram and returns its shifted combinations.
        trigram (str): an input trigram (e.g. 'the')
    """
    return get_ngram_shifted_combinations(trigram)

def find_ngram_equivalents(text: str, ngrams: list, n: int):
    """
    Converts a text into a set of n-grams, and returns the common
    n-grams between the n-grams of the text and an input n-gram list.
    """
    return list(set(get_ngrams(parse_text(text), n)).intersection(ngrams))