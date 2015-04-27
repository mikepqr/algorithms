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
    A = np.zeros((n+1, n, n), dtype=np.int) + 2147483647
    for u, vs in g.items():
        for v in vs:
            A[0, u-1, v[0]-1] = v[1]
    for i in range(n):
        A[0, i, i] = 0

    # TODO explain range
    for k in range(1, n+1):
        print k
        for i in range(n):
            for j in range(n):
                A[k, i, j] = min(
                    A[k-1, i, j],
                    A[k-1, i, k-1] + A[k-1, k-1, j]
                )

    for i in range(n):
        if A[n, i, i] < 0:
            return np.inf
    else:
        return np.min(A)
