import numpy as np
from scipy import spatial


def read_tsp(filename):
    points = []
    with open(filename, 'r') as f:
        n = int(f.readline())
        points = np.zeros((n, 2))
        for i, l in enumerate(f):
            points[i, :] = map(int, l.split())
    return n, points


def calc_euclidian_distances(points):
    return spatial.distance.squareform(spatial.distance.pdist(points))


def tsp(edges):
    pass


def test_tsp():
    linearpath = read_tsp('tsp_tests/linearpath.txt')
    assert tsp(linearpath) == 12
    rectangularpath = read_tsp('tsp_tests/rectangularpath.txt')
    assert tsp(rectangularpath) == 10
    testpath = read_tsp('tsp_tests/testpath.txt')
    assert tsp(testpath) == 3.50116
