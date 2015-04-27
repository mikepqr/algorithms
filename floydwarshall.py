from collections import defaultdict
import numpy as np

BIG_INT = int(2**31 - 1)


def read_weighted_edge_list(filename):
    edges = []
    with open(filename, 'r') as f:
        l = f.readline()
        n, m = map(int, l.split())
        for i, l in enumerate(f):
            u, v, c = map(int, l.split())
            edges.append((u, v, c))
    return n, m, edges


def convert_weighted_edge_list_to_adjacency_list(edges, directed=True):
    g = defaultdict(list)
    for u, v, c in edges:
        g[u].append((v, c))
        if not directed:
            g[v].append((u, c))

    return g


def floydwarshall(n, edges):
    '''
    Returns the minimum shortest path in a directed graph with n nodes and edge
    list edges. Uses the Floyd Warshall algorithm.
    '''
    g = convert_weighted_edge_list_to_adjacency_list(edges)

    # A is an n+1 x n+1 x n+1 array. The first dimension is indexed by k. Each
    # n+1 x n+1 array at each k is the minimum shortest path from node i to
    # node j. The values for i = 0 or j = 0 are undefined for all k. The
    # redundant 0th row/column simplifies dealing with the conventional input
    # for this problem, in which nodes are numbered 1 to n. Effectivtly it
    # turns Python into a 1-indexing language.
    #
    # int(2**31 - 1) is an arbitrary large integer (the largest possible in 32
    # bit precision), and denotes the absence of a path between two nodes
    # (which is true for all pairs of nodes not connected by 1 edge, at the
    # beginning of the code).
    A = np.zeros((n+1, n+1, n+1), dtype=np.int) + BIG_INT
    # Read in the edges.
    for u, vs in g.items():
        for v in vs:
            A[0, u, v[0]] = v[1]
    # Nodes are connected to themselves.
    for i in range(1, n+1):
        A[0, i, i] = 0

    # The Floyd Warshall considers subproblems of size k, where k is the
    # maximum number of edges that can be used to build a path from node i to
    # j. The best possible path from i to j using up to k edges is then the
    # better of:
    #  1. The path from i to j using up to k - 1 edges, and
    #  2. The path from i to w using up to k - 1 edges + the path from w to j,
    #     for all nodes w that have edges leading directly to j
    for k in range(1, n+1):
        # Matrix-manipulation trick:
        #   X[i, k] + Y[k, j] = Z[i, j] if
        #   Z = X[k, :] + A[:, k]_transpose
        # Where the calculation of the matrix Z uses broadcasting rather than a
        # double for loop. The (n+1, n+1) array B is then case 2 above
        B = A[k-1, k, :] + A[k-1, :, k][np.newaxis].T
        A[k, :, :] = np.minimum(A[k - 1, :, :], B)

    # Floyd Warshall has at least one negative number on the leading diagonal
    # is a negative weight closed cycle was found (in which case the minimum
    # shortest path is not defined).
    for i in range(1, n+1):
        if A[n, i, i] < 0:
            return BIG_INT
    else:
        return np.min(A[n, :, :])


def test_floydwarshall():
    n, m, edges = read_weighted_edge_list('apsp_tests/tc1.txt')
    assert floydwarshall(n, edges) == -10003
    n, m, edges = read_weighted_edge_list('apsp_tests/tc2.txt')
    assert floydwarshall(n, edges) == -6
    n, m, edges = read_weighted_edge_list('apsp_tests/tc3.txt')
    assert floydwarshall(n, edges) == np.inf


def solve_assignment4():
    n, m, edges = read_weighted_edge_list('apsp_tests/g1.txt')
    g1_solution = floydwarshall(n, edges)
    n, m, edges = read_weighted_edge_list('apsp_tests/g2.txt')
    g2_solution = floydwarshall(n, edges)
    n, m, edges = read_weighted_edge_list('apsp_tests/g3.txt')
    g3_solution = floydwarshall(n, edges)

    solution = min(g1_solution, g2_solution, g3_solution)
    assert solution == -19
    print solution
