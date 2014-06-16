def readIntegerFile(file):
    '''
    Reads in a file containing one integer on each line. Returns a dictionary
    (hash table) with keys of integers.
    '''
    h = {}
    with open(file, 'r') as f:
        for i in f:
            h[int(i)] = True
    return h


def exercise(test=None, verbose=False):
    '''
    >>> exercise(test=1)
    3
    >>> exercise(test=2)
    5
    >>> exercise(test=3)
    6
    '''
    if test:
        file = 'sum2_tests/sum2_tc' + str(test) + '.txt'
    else:
        file = 'sum2_tests/algo1-programming_prob-2sum.txt'

    h = readIntegerFile(file=file)

    hits = 0

    for t in range(-10000, 10001):
        if verbose and t % 100 == 0:
            print t
        for i in h.keys():
            if t - i in h and t - i != i:
                hits += 1
                break

    return hits


if __name__ == "__main__":
    import doctest
    doctest.testmod()
