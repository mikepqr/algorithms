import math
import numpy as np
import kosaraju


def read_sat2(filename):
    clauses = []
    with open(filename, 'r') as f:
        n = int(f.readline())
        for l in f:
            clauses.append(map(int, l.split()))
    return n, clauses


def convert_clauses_to_graph(clauses):
    '''
    Convert 2SAT clauses to an implication graph. A directed edge passes from u
    to -v if there is a clause requiring v to be False if u is True. E.g. a
    clause (1 or 2) is translated into the two edges (-1, 2) (not 1 implies 2)
    and and (-2, 1) (not 2 implies 1).
    '''
    edges = {}
    i = 1
    for c1, c2 in clauses:
        edges[i] = (-c1, c2)
        i += 1
        edges[i] = (-c2, c1)
        i += 1

    return edges


def kosaraju_check(clauses):
    '''
    Determines if a 2SAT problem is satisfiable by SCC analysis of the
    implication graph. Uses Kosaraju's SCC algorithm to find the SCCs of the
    implication graph. Then if any node u is in the same SCC as its negation -u
    then it is not possible to satisfy the clauses contaniing u, and the
    problem is unsatisfiable.
    '''
    edges = convert_clauses_to_graph(clauses)
    leader = kosaraju.kosaraju(edges)

    for i, l in leader.items():
        if i > 0:
            if l == leader[-i]:
                return False

    return True


def solve_week6():
    cases = [
        (read_sat2("sat2_tests/2sat1.txt"), True),
        (read_sat2("sat2_tests/2sat2.txt"), False),
        (read_sat2("sat2_tests/2sat3.txt"), True),
        (read_sat2("sat2_tests/2sat4.txt"), True),
        (read_sat2("sat2_tests/2sat5.txt"), False),
        (read_sat2("sat2_tests/2sat6.txt"), False)
    ]
    s = ''
    for c, ans in cases:
        sol = kosaraju_check(c[1])
        s += ('1' if sol else '0')
        assert sol == ans
    return s


def naive_check_sat(x, clauses):
    sat = np.zeros(len(clauses), dtype=np.bool)
    for i, (c1, c2) in enumerate(clauses):
        if c1 > 0:
            if x[c1-1]:
                sat[i] = True
        if c1 < 0:
            if not x[-c1-1]:
                sat[i] = True
        if c2 > 0:
            if x[c2-1]:
                sat[i] = True
        if c2 < 0:
            if not x[-c2-1]:
                sat[i] = True

    return sat


def naive_sat2(n, clauses):
    nouterloop = int(math.log(n, 2))
    ninnerloop = 2 * n ** 2

    i = 0
    while i <= nouterloop:
        print i
        i += 1
        x = np.random.choice([True, False], n)

        k = 0
        while k <= ninnerloop:
            print k
            k += 1
            sat = naive_check_sat(x, clauses)
            if sat.all():
                return True
            else:
                clause_fix = np.random.choice(np.where(sat == False)[0])
                xfix = np.random.choice(clauses[clause_fix])
                if xfix > 0:
                    x[xfix-1] = True
                else:
                    x[xfix+1] = False

    return False
