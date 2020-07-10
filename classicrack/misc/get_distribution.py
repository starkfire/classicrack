# This is just a script for fetching and mapping ngram frequency 
# distributions from text files.
#
# Sources:
# http://practicalcryptography.com/media/cryptanalysis/files/english_monograms.txt
# http://practicalcryptography.com/media/cryptanalysis/files/english_bigrams.txt
# http://practicalcryptography.com/media/cryptanalysis/files/english_trigrams.txt.zip
# http://practicalcryptography.com/media/cryptanalysis/files/english_quadgrams.txt.zip
# http://practicalcryptography.com/media/cryptanalysis/files/english_quintgrams.txt.zip

def get_ngrams(input_file: str, output_file: str):
    with open(input_file) as file:
        ngrams = {}
        for line in file:
            ngram, freq = line.replace('\n', '').split(' ')
            ngrams[ngram] = int(freq)

    out = open(output_file, 'w')
    out.write(str(ngrams))