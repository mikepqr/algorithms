from collections import Counter


def readEdges(file="scc_tests/tc0.txt"):
    edges = {}
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            u, v = int(line.split()[0]), int(line.split()[1])
            edges[i+1] = (u, v)
    return edges


def reverseEdges(edges):
    for i, edge in edges.iteritems():
        edges[i] = (edge[1], edge[0])

    return edges


def edgesToAdjacency(edges):
    graph = {}
    for i, edge in edges.iteritems():
        graph.setdefault(edge[0], []).append(edge[1])
    return graph


def dfs(edges, adjacencyList, i, explored, leader, f, s, t):
    # s = most recent node from which dfs was initiated
    # t = number of nodes completely processed so far
    leader[i] = s
    explored[i] = True

    if i in adjacencyList:
        for j in adjacencyList[i]:
            if not explored[j]:
                f, t = dfs(edges, adjacencyList, j, explored, leader, f, s, t)

    # totally finished exploring node i
    t += 1
    f[i] = t

    return f, t


def dfsLoop(edges, adjacencyList):
    t = 0
    n = 0
    for i in edges.itervalues():
        if n < max(i):
            n = max(i)
    n = int(n)
    print "n =", n

    explored = dict(zip(range(1, n+1), [False]*n))
    leader = dict(zip(range(1, n+1), [False]*n))
    f = dict(zip(range(1, n+1), [False]*n))

    for i in range(n, 0, -1):
        if not explored[i]:
            f, t = dfs(edges, adjacencyList, i, explored, leader, f, i, t)

    return f, leader


def kosaraju(file="scc_tests/tc0.txt"):
    edges = readEdges(file=file)
    print "Read edges file"

    edges = reverseEdges(edges)
    print "Reversed edges"

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
    print "Computed adjacency list of re-reversed edges"

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

    # Print comma-separated list of top 5 SCCs by size
    ','.join([str(scc_size) for leader, scc_size in cnt.most_common()[0:5]])
