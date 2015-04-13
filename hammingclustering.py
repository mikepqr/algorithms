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


def find_rightmost_01(y):
    for i in range(len(y)-1, -1, -1):
        if y[i:i+2] == [0, 1]:
            return i
    return -1


def hamming_nodes(ndim, d):
    '''
    Returns all nodes of Hamming weight d in ndim dimensions.

    Uses a method pinched from http://stackoverflow.com/a/27755751

    Begin with a vector of ndim - d 0s and d 1s at the end (e.g. 0011 for
    n = 4 and r = 2). Add this to the list of nodes.

    Then, repeat the following procedure:

        1. Find the rightmost sequence [0, 1] If there is no such one, we are
        done.

        2. Permute that 0 and 1. Add this to the list of nodes.

        3. Bubble all 1s to the right of that sequence to the end of the
        vector. Add this to the list of nodes.
    '''
    nodes = []
    x = (ndim - d) * [0] + d * [1]
    nodes.append(x[:])  # always append a copy of x to prevent referencing

    i = find_rightmost_01(x)
    while i != -1:
        # Permute that 0 and 1 and add new node to list of candidates
        x[i], x[i+1] = x[i+1], x[i]
        nodes.append(x[:])

        # Bubble all 1s to the right of that sequence to the end and add new
        # node to list of candidates
        bubbled = False
        for j, v in enumerate(x[:i+1:-1]):
            if v == 1:
                x.append(x.pop(ndim - j - 1))
                bubbled = True
        if bubbled:
            nodes.append(x[:])

        i = find_rightmost_01(x)

    # Convert list of nodes to list of strings of binary representation
    # e.g. [[0, 1], [1, 0], [0, 1]] -> ['01', '10', '01']
    nodes = [''.join(map(str, [k for k in n])) for n in nodes]
    # Convert all nodes to int representation
    # e.g. ['01', '10', '01'] -> [1, 2, 1]
    nodes = map(lambda x: int(x, 2), nodes)
    # Return deduplicated list
    return set(nodes)


def find_pairs(nodes, ndim, d):
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

    The number of calculations is (ndim C d) * len(nodes), e.g. for ndim = 24,
    d = 2 and len(nodes) = 2e5, you must check for the existence of 54865488
    keys.

    For large lists of nodes, this is much quicker and more tractable than the
    O(N^2) pairwise distance calcuation (and subsequent sort) required to
    naively implement K-clustering.
    '''
    pairs = set()

    # For all nodes with Hamming weight d
    for j in hamming_nodes(ndim, d):
        # For every node in nodes
        for n in nodes:
            # n^j is a distance d from n so if n^j is in nodes then n and n^j
            # are a pair of nodes separated by d that should be added to the
            # list
            target = n ^ j
            if n < target:
                if target in nodes:
                    pairs.add((n, target))

    return pairs


def hamming_clustering(nodes, min_distance):
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
        pairs = find_pairs(nodes, ndim, d)
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
