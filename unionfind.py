class UnionFind(object):
    '''
    Implements a primitive UnionFind data structure for managing clusters of
    nodes or objects.

    Example basic usage:

    >>> x = UnionFind(list('ABCDE'))
    >>> x.find('A')
    A
    >>> x.get_nodes_of_head('B')
    ['B']

    i.e. Every nodeect is its own head (i.e. in a cluster of size 1) at
    instantiation. The union operation:

    >>> x.union('A', 'B')
    >>> x.find('A')
    A
    >>> x.find('B')
    A
    >>> x.get_nodes_of_head('A')
    ['A', 'B']
    >>> x.get_heads()
    ['A', 'C', 'D', 'E']

    Internally, self.nodes_to_head is a dictionary in which the value for each
    nodeect is the head to which it points. self.head_to_nodes is a dictionary
    in which the value for each head is the list of nodeects to which it
    points. Imagine two clusters, ABC and DE. Then:

        nodes_to_head[A] = A
        nodes_to_head[B] = A
        nodes_to_head[C] = A
        nodes_to_head[D] = D
        nodes_to_head[E] = D

    and:

        head_to_nodes[A] = [A, B, C]
        head_to_nodes[D] = [D, E]

    '''

    def __init__(self, nodes):
        # Each node is its own head at instantiation
        self.nodes_to_head = dict(zip(nodes, nodes))
        self.head_to_nodes = dict(zip(nodes, [[i] for i in nodes]))

    def __str__(self):
        return str(self.head_to_nodes)

    def add(self, node):
        self.nodes_to_head[node] = node
        self.head_to_nodes[node] = [node]

    def get_nodes_of_head(self, head):
        return self.head_to_nodes[head]

    def get_heads(self):
        return self.head_to_nodes.keys()

    def find(self, node):
        return self.nodes_to_head[node]

    def union(self, node1, node2):
        head1 = self.nodes_to_head[node1]
        head2 = self.nodes_to_head[node2]
        if head1 != head2:
            # Update each node pointing to head2 such that it points to head1
            for node in self.head_to_nodes[head2]:
                self.nodes_to_head[node] = head1
            # Add all the nodes in head2's list of children to head1's list
            self.head_to_nodes[head1] += self.head_to_nodes[head2]
            # Delete head2's entry in dict of heads
            del self.head_to_nodes[head2]
        # If the nodes point to the same head, union does nothing
        else:
            return
