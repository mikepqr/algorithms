'''
Determines the shortest path from a node to all other nodes in a graph using
Dijkstra's algorithm.

The algorithm uses a list x containing processed nodes. Initially this list is
just the node x (to which the distance is 0). For all edges beginning in x and
ending outside x, calculate Dijkstra's greedy criterion a[v] + l_vw, where a[v]
is the shortest path from s to v and l_vw is the length of the edge (v, w).
Find the edge (v*, w*) that minimizes this criterion. The shortest path from s
to w*, a[w*] is then given by a[v*] + l_v*w*. Add w* to x. Repeat until x
contains all nodes in the graph.

>>> test_path = 'dijkstra_tests/dijkstra_'
>>> g = readWeightedGraph(test_path + 'tc1.txt')
>>> a = dijkstra(g, '1')
>>> a['4']
2
>>> dijkstra(readWeightedGraph(test_path + 'tc2.txt'), '1')['7']
5
>>> dijkstra(readWeightedGraph(test_path + 'tc3.txt'), '13')['5']
26
>>> dijkstra(readWeightedGraph(test_path + 'tc4.txt'), '28')['6']
9
'''


def readWeightedGraph(file='dijkstra_tests/dijkstraData.txt'):
    '''
    Returns a dictionary adjacency list representation of a graph where nodes
    are keys, the values are a list of tuples of the heads of the edges
    leaving the node, and their weights. E.g. if g['a'] = [('b',100)] then node
    a has an edge leading to node b with weight (or length) 100.
    '''
    g = {}
    with open(file, 'r') as f:
        for i in f:
            node, edges = i.split()[0], i.split()[1:]
            g[node] = [(i.split(',')[0], int(i.split(',')[1])) for i in edges]
    return g


def sumEdges(g):
    '''
    Return sum of all edges of graph (may double count, should really only be
    relied upon to return a number that is guaranteed to be at least as long
    as all paths in the graph).
    '''
    sum = 0
    for u in g.keys():
        for edge in g[u]:
            sum += edge[1]
    return sum


def dijkstra(g, s):
    '''
    Uses Dijkstra's algorithm to compute length of shortest paths from s to
    all other nodes in graph g.
    '''
    x = [s]
    a = dict(zip(g.keys(), [0]*len(g)))
    worstcase = sumEdges(g)

    while True:
        # Initialize best to a large number that all paths guaranteed to be
        # shorter than (all paths guaranteed to be no longer than sum of
        # lengths of all the edges)
        best = worstcase

        # For every node in the list of processed nodes
        for v in x:
            # For every edge leaving that node
            for edge in g[v]:
                # If that edge leads to a node outside list of processed nodes
                if edge[0] not in x:
                    # If DGC for that node is shorter than any so far, record
                    # the edge and the distance to it
                    if a[v] + edge[1] < best:
                        best = a[v] + edge[1]
                        vstar = v
                        wstar = edge[0]
                        l_vstar_wstar = edge[1]

        # Add destination of best edge chosen by DGC to list of processed nodes
        x.append(wstar)

        # Set shortest path to that node to be DGC for that node from list x
        a[wstar] = a[vstar] + l_vstar_wstar

        # If list of processed nodes the same size as graph, graph processed.
        if len(x) == len(g):
            break

    return a


def exercise():
    g = readWeightedGraph()
    a = dijkstra(g, '1')
    targets = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    print ','.join([str(a[str(i)]) for i in targets])
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()
