import random
import math
import copy


def readGraph(file='mincut_tests/kargerMinCut.txt'):
    '''
    Returns a dictionary adjacency list representation of a graph where nodes
    are keys, and the adjacent nodes for each node is the entry for its key (a
    list of 1 or more elements).
    '''
    g = {}
    with open(file, 'r') as f:
        for i in f:
            node, edges = i.split()[0], i.split()[1:]
            g[node] = edges
    return g


def deleteNode(g, u):
    '''
    Removes a node from a graph, i.e. removes its key from an graph dictionary,
    and removes all occurences from the adjacency lists in the graph

    >>> g = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'],
    ...      'D': ['C'], 'E': ['F'], 'F': ['C']}
    >>> deleteNode(g, 'C')
    {'A': ['B'], 'B': ['D'], 'E': ['F'], 'D': [], 'F': []}
    '''
    # delete node u
    if u in g:
        del g[u]

    # delete all occurences of node u in lists of edges
    for i in g:
        g[i] = [j for j in g[i] if j != u]

    return g


def deleteEdge(g, u, v, all=False):
    '''
    Removes an edge u-v from a graph. If there are parallel edges, removes
    only one edge, unless all=True, in which case all edges u-v are removed.

    >>> g = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'C']}
    >>> deleteEdge(g, 'C', 'A')
    {'A': ['B'], 'C': ['B', 'C'], 'B': ['A', 'C']}
    '''

    if all:
        g[u] = [i for i in g[u] if i != v]
        g[v] = [i for i in g[v] if i != u]
    else:
        # Remove one occurence of v from u's list of edges
        g[u].remove(v)
        # vice versa
        g[v].remove(u)

    return g


def selectRandomEdge(g):
    '''
    Returns a random edge (u,v) from a graph.
    '''
    u, v = None, None
    while not v:
        u = random.choice(g.keys())
        if g[u]:
            v = random.choice(g[u])
    return u, v


def mergeEdge(g, u, v):
    '''
    Merges an edge of a graph, i.e. deletes all edges between the nodes u and
    v, assigns all v's edges to u, replaces all occurences of v in other
    adjacency lists with u, and deletes the node v from the graph.
    '''
    # Delete edge u-v
    g = deleteEdge(g, u, v, all=True)

    # u inherits all v's edges
    g[u] += g[v]

    # replace all occurences of v in lists of edges with u
    for i in g:
        g[i] = [u if j == v else j for j in g[i]]

    g = deleteNode(g, v)
    return g


def randomContraction(g):
    '''
    Implements a single trial of Karger's min cut algorithm to determine the
    minimum number of cuts required to split a graph in two. See minCut() for
    further details.
    '''
    while len(g) > 2:
        u, v = selectRandomEdge(g)
        g = mergeEdge(g, u, v)
    return g.keys(), len(g[g.keys()[0]])


def minCut(gorig, verbose=False):
    '''
    Implements a single trial of Karger's min cut algorithm to determine the
    minimum number of cuts required to split a graph in two sets A and B.

    Calls randomContraction() n^2 logn times. randomContraction() merges nodes
    of the graph gorig until two nodes remain. The number of edges connecting
    the nodes is then the nubmer of cuts required for that random choice of A
    and B.

    By calling randomContraction() ~n^2 logn times, the probability that the
    minimum number of cuts returned by this algorithm is *greater* than the
    true minimum number of cuts is ~1/n.
    '''
    n = len(gorig)
    min = n**2
    for i in range(int(math.log(n) * n**2)):
        g = copy.deepcopy(gorig)
        k, cuts = randomContraction(g)
        if cuts < min:
            min = cuts
            bestk = k
        if verbose and i % 10 == 0:
            print i, bestk, min

    return min


if __name__ == "__main__":
    import doctest
    doctest.testmod()
