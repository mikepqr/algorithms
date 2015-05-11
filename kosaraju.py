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


def dfs(edges, adjacencyList, i, discovered, leader, f, s, t):
    '''
    Given a graph (a dict of edges and a dict adjacency list), a starting
    node i, a parent node s (=i for initial call of dfs), and t (running count
    of number of nodes completely explored, conduct recursive DFS on graph,
    returning rank order in which node i completely explored.

    Side-effects: updates the key i in these dicts:
     - discovered (discovered flag)
     - leader (id of origin node from which node was discovered, i.e. starting
       node for original call of dfs in dfsLoop)
     - f (finishing time, i.e.  rank order in which paths from node fully
       explored).

    Returns t.
    '''

    # Mark i discovered
    discovered[i] = True

    # Leader of node i is s by definition of function spec
    leader[i] = s

    # If there are edges leaving i in in the adjacency list
    if i in adjacencyList:
        # For each destination of edges leaving i
        for j in adjacencyList[i]:
            # If destination undiscovered
            if not discovered[j]:
                # Recursively DFS on graph using that destination as starting
                # point
                t = dfs(edges, adjacencyList, j, discovered, leader, f, s, t)

    # Have now totally finished exploring i and all nodes reachable from i.
    # Update running count of nodes completely explored, and finishing time of
    # node i
    t += 1
    f[i] = t

    return t


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
    nodes = set()
    for u, v in edges.itervalues():
        nodes.add(u)
        nodes.add(v)
    nodes = sorted(list(nodes), reverse=True)
    n = len(nodes)

    # initialize dictionaries
    # discovered = boolean dict of {node: discovered flag}
    # leader = dict of {node: origin node from which it was discovered}
    # f = dict of finishing times {node: rand order in which paths from node
    # fully explored
    discovered = dict(zip(nodes, [False]*n))
    leader = dict(zip(nodes, [False]*n))
    f = dict(zip(nodes, [False]*n))

    # initialize finishing time, i.e. number of nodes completely processed
    t = 0

    # For all nodes, counting down from node n to node 1 (nodes is pre-sorted)
    for i in nodes:
        # If node undiscovered
        if not discovered[i]:
            # Run DFS on graph using node i as starting point; keeping track of
            # discovered, leader, f, t; using i as leader for all nodes
            # discovered from this call
            t = dfs(edges, adjacencyList, i, discovered, leader, f, i, t)

    return f, leader


def kosaraju(edges):
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

    edges = reverseEdges(edges)
    adjacencyList = edgesToAdjacency(edges)
    f1, leader1 = dfsLoop(edges, adjacencyList)

    for i, edge in edges.iteritems():
        edges[i] = (f1[edge[0]], f1[edge[1]])

    edges = reverseEdges(edges)
    adjacencyList = edgesToAdjacency(edges)
    f2, leader2 = dfsLoop(edges, adjacencyList)

    # Build inverted dictionary to look up original node names
    f1inv = {v: k for k, v in f1.items()}
    # Build dictionary of leader2 relablled with original node names
    leader = {}
    for i, l in leader2.items():
        leader[f1inv[i]] = f1inv[l]

    return leader


def count_scc_size(leader):
    cnt = Counter()
    for l in leader.itervalues():
        cnt[l] += 1
    return cnt


def test_kosaraju():
    e1 = readEdges("scc_tests/tc1.txt")
    e2 = readEdges("scc_tests/tc2.txt")
    e3 = readEdges("scc_tests/tc3.txt")
    e4 = readEdges("scc_tests/tc4.txt")
    e5 = readEdges("scc_tests/tc5.txt")
    e6 = readEdges("scc_tests/tc6.txt")
    e7 = readEdges("scc_tests/tc7.txt")
    assert sorted(count_scc_size(kosaraju(e1)).values(), reverse=True) == [
        3, 3, 3]
    assert sorted(count_scc_size(kosaraju(e2)).values(), reverse=True) == [
        3, 3, 2]
    assert sorted(count_scc_size(kosaraju(e3)).values(), reverse=True) == [
        3, 3, 1, 1]
    assert sorted(count_scc_size(kosaraju(e4)).values(), reverse=True) == [
        7, 1]
    assert sorted(count_scc_size(kosaraju(e5)).values(), reverse=True) == [
        6, 3, 2, 1]
    assert sorted(count_scc_size(kosaraju(e6)).values(), reverse=True) == [
        35, 7, 1, 1, 1, 1, 1, 1, 1, 1]
    assert sorted(count_scc_size(kosaraju(e7)).values(), reverse=True) == [
        917, 313, 167, 37, 3]


def exercise():
    '''
    Solve Algorithms 1, exercise 4.
    '''
    # Magic to set resources as generously as possible to avoid recursion limit
    # and segfaults when memory runs out
    import sys
    sys.setrecursionlimit(2**20)
    import resource
    resource.setrlimit(resource.RLIMIT_STACK, (1.5*2**25, 1.5*2**25))

    edges = readEdges("scc_tests/SCC.txt")
    leader = kosaraju(edges)
    cnt = count_scc_size(leader)

    # Print comma-separated list of top 5 SCCs by size, as requested by
    # exercise.
    print ','.join([str(scc_size) for l, scc_size in cnt.most_common()[0:5]])
    assert cnt.most_common()[0:5] == [434821, 968, 459, 313, 211]
