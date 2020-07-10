from classicrack.utils.common import frequency, probability_distribution

def chi_squared(texts: list, fd: dict):
    """
    Uses chi-squared test to calculate the fitness of a plaintext.
        texts (list): a list of texts
        fd (dict): reference frequency distribution (e.g. English alphabet distribution)
    """
    pd = probability_distribution(fd)
    fd = [frequency(texts[x]) for x in range(len(texts))]
    chi_sq = {}
    
    for x in range(len(fd)):
        csq = 0
        for y in texts[x]:
            observed = fd[x]
            expected = pd[y.upper()] * len(texts[x])
            csq += pow((observed[y] - expected), 2) / expected
        chi_sq.update({texts[x] : csq})

    return chi_sq