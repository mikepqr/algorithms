from collections import defaultdict


def read_weighted_edge_list(filename):
    edges = []
    with open(filename, 'r') as f:
        l = f.readline()
        n, m = map(int, l.split())
        for i, l in enumerate(f):
            u, v, c = map(int, l.split())
            edges.append((u, v, c))
    return n, m, edges


def convert_weighted_edge_list_to_adjacency_list(edges):
    g = defaultdict(list)
    for u, v, c in edges:
        g[u].append((v, c))
        g[v].append((u, c))

    return g


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
    longest_edge = max([c for u, v, c in edges])

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
