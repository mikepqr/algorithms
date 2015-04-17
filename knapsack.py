import numpy as np


def read_knapsack(filename):
    '''
    Returns a tuple whose elements are:

     - the knapsack size
     - the number of items
     - a 2xN numpy array denoting the items. The 0th element of each
    row is the value of the item, and the first is the weight.

    '''
    with open(filename, 'r') as f:
        W, n = map(int, f.readline().split())
        items = np.zeros((n, 2), dtype=np.int)

        for i, l in enumerate(f):
            items[i, :] = map(int, l.split())

    return W, n, items


def knapsack(W, items):
    '''
    Return the maximum possible value of the knapsack problem, i.e. the total
    value of the items in the knapsack, where items have value v0, v1 .. vn and
    weight w0, w1 .. wn, subject to the constraint that the sum of the weights
    of the selected items must be no more than W.

    W is an integer capacity for the knapsack. items is a 2xN array
    denoting the items that may be selected. The 0th element of each row is the
    value of the item, and the first is the weight.
    '''

    n = len(items)
    # A[i, x] stores the solution to the optimal knapsack problem for items
    # 0..i-1 and a knapsack of capacity x (-1 handles Python's 0-indexed
    # arrays).
    A = np.zeros((n+1, W+1), dtype=np.int)

    # A[0, x] = 0 for x = 0, 1, 2 .. W
    # i.e. populate the array A from bottom up
    for i in range(1, n+1):
        # The value and weight of the current current item (-1 handles Python's
        # 0-indexed arrays).
        vi = items[i-1, 0]
        wi = items[i-1, 1]

        # The knapsack recursion
        for x in range(0, W+1):
            if wi <= x:
                A[i, x] = max(A[i-1, x], A[i-1, x-wi] + vi)
            else:
                A[i, x] = A[i-1, x]

    return A[n, W]


def knapsack_lowmem(W, items):
    '''
    As knapsack() but with a lower memory requirement. Instead of storing a nxW
    array, stores two length W arrays. This is possible because the recursion
    for A[i, :] is a function only of A[i-1, :].
    '''

    n = len(items)
    # For the current value of i, A[x] stores the solution to the optimal
    # knapsack problem for items 0..i-1 and a knapsack of capacity x (-1
    # handles Python's 0-indexed arrays).
    A = np.zeros(W+1, dtype=np.int)
    # For the current value of i, B[x] stores the solution to the optimal
    # knapsack problem for items 0..i-2 and a knapsack of capacity x (-1
    # handles Python's 0-indexed arrays).
    B = np.zeros(W+1, dtype=np.int)

    # A[0, x] = 0 for x = 0, 1, 2 .. W
    for i in range(1, n+1):
        vi = items[i-1, 0]
        wi = items[i-1, 1]

        for x in range(0, W+1):
            if wi <= x:
                A[x] = max(B[x], B[x-wi] + vi)
            else:
                A[x] = B[x]

        B = A.copy()

    return A[W]


def knapsack_recursive(W, items, A=None, B=None):
    '''
    As knapsack() but calculates A[n, W] with recursive calls. It therefore
    calculates only the optimal knapsack for those subproblems that are
    strictly necessary to calculate the problem.

    The array B is a boolean nxW B[i, x] is True if the recursion has already
    calculated the optimal knapsack for the subproblem for items[0:i] and w =
    x. Therefore at any time np.sum(B) is the number of optimal knapsack
    problems that have been solved.

    For large problems, this can be << nW. E.g. for the file knapsack_big.txt,
    where W=200,000 and n=2000, only 0.3% of the 4e8 subproblems need be
    considered.
    '''

    i = len(items)
    if A is None:
        A = np.zeros((i+1, W+1), dtype=np.int)
    if B is None:
        B = np.zeros((i+1, W+1), dtype=np.bool)

    # A[0, :] = 0 for all x, so we're done.
    if i == 0:
        B[i, :] = True
        return A[i, W]
    else:
        # If we've already calculated the optimal knapsack value for
        # items[0:i-1], capacity W then that's one possible value for this
        # problem
        if B[i-1, W]:
            term1 = A[i-1, W]
        # If not, calculate that optimal knapsack value
        else:
            term1 = knapsack_recursive(W, items[0:i-1], A, B)

        # The value and weight of the current current item (-1 handles Python's
        # 0-indexed arrays).
        vi = items[i-1, 0]
        wi = items[i-1, 1]

        if wi <= W:
            # If we've already calculated the optimal knapsack value for
            # items[0:i-1], capacity W-wi then that's one possible value for
            # this problem
            if B[i-1, W-wi]:
                term2 = A[i-1, W-wi] + vi
            # If not, calculate that optimal knapsack value plus current item
            # value
            else:
                term2 = knapsack_recursive(W-wi, items[0:i-1], A, B) + vi
        else:
            term2 = 0

        # The optimal knapsack for items[0:i], capacity W is the greater of
        # term1 and term2
        A[i, W] = max(term1, term2)
        B[i, W] = True
        return A[i, W]


def test_knapsack():
    W, n, items = read_knapsack('knapsack_tests/tc1.txt')
    solution = 8
    assert knapsack(W, items) == solution
    assert knapsack_lowmem(W, items) == solution
    assert knapsack_recursive(W, items) == solution

    W, n, items = read_knapsack('knapsack_tests/knapsack1.txt')
    solution = 2493893
    assert knapsack(W, items) == solution
    assert knapsack_lowmem(W, items) == solution
    assert knapsack_recursive(W, items) == solution
    print solution


def solve_q2():
    solution = 4243395
    W, n, items = read_knapsack('knapsack_tests/knapsack_big.txt')
    assert knapsack_recursive(W, items) == solution
    print solution
