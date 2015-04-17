import numpy as np


def obst(p):
    '''
    Returns the average cost of the Optimal Binary Search tree of a set of n
    items with probability p = [p0, p1, p2 .. pn-1], where the items are
    labelled in ascending numerical order. E.g. if the probability of searching
    for a 1, 6 and 2 are 0.2, 0.3 and 0.5, then set p = [0.2, 0.5, 0.3].
    '''
    n = len(p)
    A = np.zeros((n, n))

    for s in range(0, n):
        for i in range(0, n-s):
            term1 = sum(p[i:i+s+1])
            term2s_plus_term3s = []
            for r in range(i, i+s+1):
                if i > r-1:
                    term2 = 0
                else:
                    term2 = A[i, r-1]
                if r+1 > i+s:
                    term3 = 0
                else:
                    term3 = A[r+1, i+s]
                term2s_plus_term3s.append(term2 + term3)

            if term2s_plus_term3s:
                A[i, i+s] = term1 + min(term2s_plus_term3s)
            else:
                A[i, i+s] = term1

    return A


def solve_week3_ex5():
    s = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
    A = obst(s)
    return A[0, len(s) - 1]
