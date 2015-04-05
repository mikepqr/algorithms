from collections import defaultdict
from functools import reduce


def read_weighted_edge_list(filename):
    edges = []
    with open(filename, 'r') as f:
        l = f.readline()
        n, m = map(int, l.split())
        for i, l in enumerate(f):
            u, v, c = map(int, l.split())
            edges.append((u, v, c))
    return n, m, edges


def get_longest_edge(g):
    '''
    Returns the longest edge in a list of edges, e.g.
    >>> get_longest_edge([(1, 2, 4), (2, 3, 5), (1, 3, -9)])
    (2, 3, 5)
    '''
    edges = convert_weighted_adjacency_list_to_edge_list(g)
    return reduce(lambda x, y: x if x[2] > y[2] else y, edges)


def convert_weighted_edge_list_to_adjacency_list(edges):
    g = defaultdict(list)
    for u, v, c in edges:
        g[u].append((v, c))
        g[v].append((u, c))

    return g


def convert_weighted_adjacency_list_to_edge_list(g):
    edges = []
    for u, vcs in g.items():
        for v, c in vcs:
            if (v, u, c) not in edges:
                edges.append((u, v, c))

    return edges


def get_prim_mst(edges, s=False):
    '''
    Compute the minimum spanning tree of an undirected connected graph using
    Prim's algorithm.

    Graph must be input as a weighted edge list.

    You may optionally specify the node from which to begin the search. The
    default value is the min() of the list of nodes in the edge list. (In
    principle the result does not depend on this choice, so this is for
    testing.)
    '''
    # Convert edge list to adjacency list to avoid searching full edge list
    # each time you need every edge leaving a node.
    g = convert_weighted_edge_list_to_adjacency_list(edges)
    nodes = set(g.keys())
    if not s:
        s = min(nodes)
    longest_edge = get_longest_edge(g)[2]

    x = set([s])  # initialize list of processed nodes to be set containing s
    mst_edges = []  # this will accumulate list of edges in the MST
    total_cost = 0  # this will accumulate total cost of MST

    while True:
        # Initialize best to a number >= length of all edges to ensure an edge
        # selected on each while loop
        best = longest_edge

        # For every node in the list of processed nodes
        for u in x:
            # For every edge leaving that node
            for e in g[u]:
                # If that edge leads to a node outside list of processed nodes
                if e[0] not in x:
                    # If that edge is shorter than longest edge seen so far
                    if e[1] < best:
                        # Record u, v, and cost
                        ustar = u
                        vstar = e[0]
                        best = e[1]

        # Add destination of best edge to list of processed nodes
        x.add(vstar)
        mst_edges.append((ustar, vstar))
        total_cost += best

        # If processed nodes == nodes, you're done.
        if x == nodes:
            break

    return mst_edges, total_cost
