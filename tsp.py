import itertools
import numpy as np
from scipy import spatial


def read_tsp(filename):
    nodes = []
    with open(filename, 'r') as f:
        n = int(f.readline())
        nodes = np.zeros((n, 2))
        for i, l in enumerate(f):
            nodes[i, :] = map(float, l.split())
    return n, nodes


def calc_euclidian_distances(nodes):
    return spatial.distance.squareform(spatial.distance.pdist(nodes))


def bintuple(s):
    return sum([2**(i-1) for i in s if i > 0])


def tsp(nodes):
    n = len(nodes)
    C = calc_euclidian_distances(nodes)
    A = np.zeros((1 + bintuple(range(1, n)), n)) + np.inf
    A[bintuple([0]), 0] = 0

    for m in range(2, n+1):
        print m
        for s in itertools.combinations(range(1, n), m-1):
            s = (0,) + s
            this_bintuple = bintuple(s)
            for j in s[1:]:
                last_bintuple = this_bintuple - 2**(j-1)
                A[this_bintuple, j] = min(
                    [A[last_bintuple, k] + C[k, j]
                     for k in s if k != j]
                )

    return min([A[bintuple(s), j] + C[j, 0] for j in range(1, n)])


def test_tsp():
    n, linearnodes = read_tsp('tsp_tests/linearpath.txt')
    assert tsp(linearnodes) == 12
    n, rectangularnodes = read_tsp('tsp_tests/rectangularpath.txt')
    assert tsp(rectangularnodes) == 10
    n, testnodes = read_tsp('tsp_tests/testpath.txt')
    assert tsp(testnodes) == 3.5011560715090897


def solve_week5():
    n, nodes = read_tsp('tsp_tests/tsp.txt')
    l = tsp(nodes)
    assert l == 26442
    return int(l)
