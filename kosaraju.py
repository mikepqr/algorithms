from collections import Counter


def readEdges(file="scc_tests/tc6.txt"):
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


def edgesOfNode(edges, u):
    return dict([(k, r) for k, r in edges.iteritems() if r[0] == u])


def dfs(edges, i, explored, leader, f, s, t):
    # s = most recent node from which dfs was initiated
    # t = number of nodes completely processed so far
    leader[i] = s
    explored[i] = True

    # for each edge i,j beginning with i
    for edge in edgesOfNode(edges, i).itervalues():
        j = edge[1]
        if not explored[j]:
            f, t = dfs(edges, j, explored, leader, f, s, t)

    # totally finished exploring node i
    t += 1
    f[i] = t
    if t % 100 == 0:
        print "Processed", t, "nodes"

    return f, t


def dfsLoop(edges):
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
            f, t = dfs(edges, i, explored, leader, f, i, t)

    return f, leader


def kosaraju(file="scc_tests/tc5.txt"):
    # read edges
    edges = readEdges(file=file)
    print "Read file"

    # reverse edges
    edges = reverseEdges(edges)
    print "Reversed edges"

    # call dfsLoop on edges to get finishing times
    f, leader = dfsLoop(edges)
    print "Called dfsLoop to get finishing times"

    # relabel edges
    for i, edge in edges.iteritems():
        edges[i] = (f[edge[0]], f[edge[1]])
    print "Relabelled edges"

    # re-reverse edges
    edges = reverseEdges(edges)
    print "Reversed edges"

    f, leader = dfsLoop(edges)
    print "Called dfsLoop to get SCCs"

    # count occurences of each leader (i.e. size of groups)
    cnt = Counter()
    for l in leader.itervalues():
        cnt[l] += 1
    print "Accumulated leader counts to get SCC sizes"

    return cnt
