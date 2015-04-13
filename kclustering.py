import unionfind


def read_cluster_distances(filename):
    distances = []
    with open(filename, 'r') as f:
        n = int(f.readline())
        for i, l in enumerate(f):
            u, v, d = map(int, l.split())
            distances.append((u, v, d))
    return n, distances


def kclustering(distances_unsorted, k):
    # Get list of all nodes in distance list
    nodes = set()
    for u, v, d in distances_unsorted:
        nodes.add(u)
        nodes.add(v)

    # Create UnionFind to store clusters
    x = unionfind.UnionFind(nodes)

    # Sort [(u, v, d)] list on ascending d so we can pop off shortest edges
    # first
    distances = sorted(distances_unsorted, key=lambda x: x[2])

    # Single-link clustering loop: while > k clusters, merge clusters
    # containing closest nodes
    while len(x.get_heads()) > k:
        u, v, d = distances.pop(0)
        x.union(u, v)

    # In the event of ties (?), distances may contain pairs that are now in
    # the same cluster, but the first element in distances for which
    # this is not true is the closest pair not in the same cluster.
    while True:
        u, v, min_distance = distances.pop(0)
        if x.find(u) != x.find(v):
            break

    return x, min_distance
