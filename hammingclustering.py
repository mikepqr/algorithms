import itertools
import unionfind


def read_nodes(filename):
    '''
    Returns a dict whose:

     - keys are the *integer* representations of the binary numbers in filename
       (one binary number per line)

     - values are the number of occurences of that number in file.
    '''
    nodes = {}
    with open(filename, 'r') as f:
        n, ndim = map(int, f.readline().split())
        for i, l in enumerate(f):
            num = int(''.join(l.split()), 2)
            if num in nodes:
                nodes[num] += 1
            else:
                nodes[num] = 1
    return nodes


def hamming_nodes(ndim, d):
    '''
    Yields all nodes of Hamming weight d in ndim dimensions.
    '''
    # Construct all ndim length combinatations of 0s and 1s
    for i in itertools.product([0, 1], repeat=ndim):
        # If combination has Hamming weight d (i.e. contains d 1s), yield it
        if i.count(1) == d:
            # Yield the integer representation
            yield int(''.join(map(str, i)), 2)


def find_pairs(nodes, ndim, d, verbose=False):
    '''
    Finds all pairs in the list of points nodes separated by Hamming distance
    d.

    This algorithm takes advantage of the fact that if A and B are binary
    vectors then the Hamming weight of A XOR B is their Hamming distance.

    It further takes advantage of the fact that, if A XOR B == D, then A XOR D
    == B.

    Together these facts imply that you can find every pairwise combination in
    nodes separated by distance d by:

     - constructing all points with Hamming weight d
     - XORing every element of nodes with each of these points
     - searching nodes for the result of that calculation

    If found, these nodes are a distance d apart.

    For large lists of nodes, this is much quicker and more tractable than the
    O(N^2) pairwise distance calcuation (and subsequent sort) required to
    naively implement K-clustering.
    '''
    if verbose:
        print "ndim = {}, d = {}".format(ndim, d)
    pairs = set()

    # For all nodes with Hamming weight d
    for j in hamming_nodes(ndim, d):
        # For every node in nodes
        for n in nodes:
            # n^j is a distance d from n so if n^j is in nodes then n and n^j
            # are a pair of nodes separated by d that should be added to the
            # list
            target = n ^ j
            if verbose:
                print "{:04b} XOR j = {:04b}".format(n, target)
            if target in nodes:
                if verbose:
                    print "{:04b} found!".format(n ^ j)
                pairs.add((n, target) if n < target else (target, n))

    return pairs


def hamming_clustering(nodes, min_distance, verbose=False):
    '''
    Performs clustering on a list of nodes whose position is expressed as a
    binary sequence in ndimensional space.

    Requires a function find_pairs() that finds all pairs of nodes separated by
    a given Hamming distance, i.e. the number of bits that must be flipped to
    make two numbers identical (e.g. the Hamming distance from 1010 to 1001 is
    2).

    Returns the UnionFind object representation of the clusters.

    >>> nodes = read_nodes('kclustering_tests/tcbig1.txt')
    >>> print hamming_clustering(nodes, 2)
    Found 15 edges with length 1
    {6: [6, 7, 4, 5, 0, 1, 3, 2, 8, 9]}
    >>> nodes = read_nodes('kclustering_tests/tcbig2.txt')
    >>> print hamming_clustering(nodes, 2)
    Found 2 edges with length 1
    {1: [1, 3, 2], 13: [13]}
    '''

    # Get maximum length of binary representation of nodes, i.e. ndim
    ndim = max(map(len, map("{:b}".format, nodes.keys())))

    # Create UnionFind to store clusters
    x = unionfind.UnionFind(nodes.keys())

    for d in range(1, min_distance):
        pairs = find_pairs(nodes, ndim, d, verbose=verbose)
        npairs = len(pairs)
        print "Found {} edges with length {}".format(npairs, d)
        for i, pair in enumerate(pairs):
            x.union(*pair)

    return x


def solve_problem2():
    '''
    Solves problem 2, i.e. returns the number of clusters when all points
    within a Hamming distance of 2 of each other have been merged.
    '''
    nodes = read_nodes('kclustering_tests/clustering_big.txt')
    x = hamming_clustering(nodes, 3)
    assert len(x.get_heads()) == 6118
    return len(x.get_heads())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
