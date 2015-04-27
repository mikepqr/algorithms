from collections import defaultdict
import numpy as np


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
    g = convert_weighted_edge_list_to_adjacency_list(edges)
    A = np.zeros((n+1, n+1, n+1), dtype=np.int) + 200000
    for u, vs in g.items():
        for v in vs:
            A[0, u, v[0]] = v[1]
    for i in range(1, n+1):
        A[0, i, i] = 0

    for k in range(1, n+1):
        # Matrix-manipulation speedup:
        #   X[i, k] + Y[k, j] = Z[i, j] if
        #   Z = X[k, :] + A[:, k]_transpose
        # Where the calculation of the matrix Z uses broadcasting rather than a
        # double for loop
        B = A[k-1, k, :] + A[k-1, :, k][np.newaxis].T
        A[k, :, :] = np.minimum(A[k - 1, :, :], B)

    for i in range(1, n+1):
        if A[n, i, i] < 0:
            return np.inf
    else:
        return np.min(A[n, :, :])
