from collections import Counter


def readEdges(file):
    '''
    Get a dictionary of edges from file. Each entry is id: (u, v), where id
    is line number in file, and tuple (u, v) is tail and head of edge.
    '''
    edges = {}
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            u, v = int(line.split()[0]), int(line.split()[1])
            edges[i+1] = (u, v)
    return edges


def reverseEdges(edges):
    '''
    Reverses a dict of edges. Returns reversed dict, but also reverses in
    place.
    '''
    for i, edge in edges.iteritems():
        edges[i] = (edge[1], edge[0])

    return edges


def edgesToAdjacency(edges):
    '''
    Derives an adjacency dict from a dict of edges. Given a dict of id: (u, v)
    where id is arbitrary unique id for each edge, and (u, v) is tail and head
    of edge, this function returns a dict of u: [vs], where u is a node and
    [vs] is a list of nodes reachable directly from u.
    '''
    graph = {}
    for i, edge in edges.iteritems():
        graph.setdefault(edge[0], []).append(edge[1])
    return graph


def dfs(edges, adjacencyList, i, explored, leader, f, s, t):
    '''
    Given a graph (a dict of edges and a dict adjacency list), a starting
    node i, a parent node s (=i for initial call of dfs), and t (running count
    of number of nodes completely explored, conduct recursive DFS on graph.

    Updates the key i in dicts explored (explored flags), leader (id of origin
    node from which node was discovered) and f (finishing time, i.e. rank order
    in which paths from node fully explored).

    Returns f and t.
    '''

    # Mark i explored
    explored[i] = True

    # Leader of node i is s by definition of function spec
    leader[i] = s

    # If there are edges leaving i in in the adjacency list
    if i in adjacencyList:
        # For each destination of edges leaving i
        for j in adjacencyList[i]:
            # If destination unexplored
            if not explored[j]:
                # Recursively DFS on graph using that destination as starting
                # point
                f, t = dfs(edges, adjacencyList, j, explored, leader, f, s, t)

    # Have now totally finished exploring i and all nodes reachable from i.
    # Update running count of nodes completely explored, and finishing time of
    # node i
    t += 1
    f[i] = t

    return f, t


def dfsLoop(edges, adjacencyList):
    '''
    Given a dict of edges {id: (u, v)} and a corresponding adjacency list
    {u: [vs]}, returns a tuple containing:

    1. the finishing times of a complete DFS search of the graph, i.e. a dict
       of {u: rank order in which paths from each node are fully explored}.

    2. the leader for each node, i.e. dict of {node: origin node from which it
       was discovered}
    '''

    # count number of nodes in graph
    n = 0
    for i in edges.itervalues():
        if n < max(i):
            n = max(i)
    n = int(n)
    print "n =", n

    # initialize dictionaries
    # explored = boolean dict of {node: explored flag}
    # leader = dict of {node: origin node from which it was discovered}
    # f = dict of finishing times {node: rand order in which paths from node
    # fully explored
    explored = dict(zip(range(1, n+1), [False]*n))
    leader = dict(zip(range(1, n+1), [False]*n))
    f = dict(zip(range(1, n+1), [False]*n))

    # initialize finishing time, i.e. number of nodes completely processed
    t = 0

    # For all nodes, counting down from node n to node 1
    for i in range(n, 0, -1):
        # If node unexplored
        if not explored[i]:
            # Run DFS on graph using node i as starting point; keeping track of
            # explored, leader, f, t; using i as leader for all nodes
            # discovered from this call
            f, t = dfs(edges, adjacencyList, i, explored, leader, f, i, t)

    return f, leader


def kosaraju(file="scc_tests/tc0.txt"):
    '''
    Implements the Kosaraju algorithm to determine the Strongly Coupled
    Components of a graph, i.e. the components of a graph within which all
    nodes can be reached from all other nodes.

    The algorithm works by running dfsLoop on the reversed graph, with aribrary
    ordering. This yields a finishing times, i.e. 'magic ordering' for the
    subsequent call of dfsLoop on the unreversed graph. This ordering
    guarantees that each call of dfs within dfsLoop discovers all members of a
    single SCC.
    '''

    edges = readEdges(file=file)
    print "Read edges file"

    edges = reverseEdges(edges)
    print "Reversed edges"

    # Compute the adjacency list for reversed edges. Massive speedup through
    # pre-computing this, rather than searching the list of edges every time to
    # find edges starting with each node.
    adjacencyList = edgesToAdjacency(edges)
    print "Computed adjacency list of reversed edges"

    f, leader = dfsLoop(edges, adjacencyList)
    print "Called dfsLoop to get finishing times"

    for i, edge in edges.iteritems():
        edges[i] = (f[edge[0]], f[edge[1]])
    print "Relabelled edges"

    edges = reverseEdges(edges)
    print "Reversed edges"

    adjacencyList = edgesToAdjacency(edges)
    print "Computed adjacency list of unreversed edges"

    f, leader = dfsLoop(edges, adjacencyList)
    print "Called dfsLoop to get SCCs"

    cnt = Counter()
    for l in leader.itervalues():
        cnt[l] += 1
    print "Accumulated leader counts to get SCC sizes"

    return cnt


if __name__ == "__main__":
    # Magic to set resources as generously as possible to avoid recursion limit
    # and segfaults when memory runs out
    import sys
    sys.setrecursionlimit(2**20)
    import resource
    resource.setrlimit(resource.RLIMIT_STACK, (1.5*2**25, 1.5*2**25))

    cnt = kosaraju(file="scc_tests/SCC.txt")

    # Print comma-separated list of top 5 SCCs by size, as requested by
    # exercise.
    ','.join([str(scc_size) for leader, scc_size in cnt.most_common()[0:5]])
