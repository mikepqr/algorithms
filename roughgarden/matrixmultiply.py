import numpy as np


def strassen_matrixmultiply(x, y):
    '''
    Multiply (dot product) of two square matrices using Strassen's
    divide-and-conquer algorithm. Matrices x and y must be of the same
    dimension n x n, and n must be an integer power of 2, e.g. 1x1, 2x2, 4x4.

    >>> x = np.array([[1, 2], [3, 4]])
    >>> y = np.array([[5, 6], [7, 8]])
    >>> strassen_matrixmultiply(x, y)
    array([[ 19.,  22.],
           [ 43.,  50.]])
    >>> x = np.arange(1,17).reshape(4,4)
    >>> y = np.arange(1,17).reshape(4,4) + 16
    >>> strassen_matrixmultiply(x, y)
    array([[  250.,   260.,   270.,   280.],
           [  618.,   644.,   670.,   696.],
           [  986.,  1028.,  1070.,  1112.],
           [ 1354.,  1412.,  1470.,  1528.]])
    '''

    n = len(x[0])
    if n == 1:
        return x * y
    m = n//2
    a = x[:m, :m]
    b = x[:m, m:]
    c = x[m:, :m]
    d = x[m:, m:]
    e = y[:m, :m]
    f = y[:m, m:]
    g = y[m:, :m]
    h = y[m:, m:]

    P1 = strassen_matrixmultiply(a, f - h)
    P2 = strassen_matrixmultiply(a + b, h)
    P3 = strassen_matrixmultiply(c + d, e)
    P4 = strassen_matrixmultiply(d, g - e)
    P5 = strassen_matrixmultiply(a + d, e + h)
    P6 = strassen_matrixmultiply(b - d, g + h)
    P7 = strassen_matrixmultiply(a - c, e + f)

    result = np.zeros((n, n))

    result[:m, :m] = P5 + P4 - P2 + P6
    result[:m, m:] = P1 + P2
    result[m:, :m] = P3 + P4
    result[m:, m:] = P1 + P5 - P3 - P7

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()


def naive_dc_matrixmultiply(x, y):
    '''
    Multiply (dot product) of two square matrices using the naive
    divide-and-conquer algorithm. Matrices x and y must be of the same
    dimension n x n, and n must be an integer power of 2, e.g. 1x1, 2x2, 4x4.

    >>> x = np.array([[1, 2], [3, 4]])
    >>> y = np.array([[5, 6], [7, 8]])
    >>> naive_dc_matrixmultiply(x, y)
    array([[ 19.,  22.],
           [ 43.,  50.]])
    >>> x = np.arange(1,17).reshape(4,4)
    >>> y = np.arange(1,17).reshape(4,4) + 16
    >>> naive_dc_matrixmultiply(x, y)
    array([[  250.,   260.,   270.,   280.],
           [  618.,   644.,   670.,   696.],
           [  986.,  1028.,  1070.,  1112.],
           [ 1354.,  1412.,  1470.,  1528.]])
    '''

    n = len(x[0])
    if n == 1:
        return x * y
    m = n//2
    a = x[:m, :m]
    b = x[:m, m:]
    c = x[m:, :m]
    d = x[m:, m:]
    e = y[:m, :m]
    f = y[:m, m:]
    g = y[m:, :m]
    h = y[m:, m:]

    A = naive_dc_matrixmultiply(a, e) + naive_dc_matrixmultiply(b, g)
    B = naive_dc_matrixmultiply(a, f) + naive_dc_matrixmultiply(b, h)
    C = naive_dc_matrixmultiply(c, e) + naive_dc_matrixmultiply(d, g)
    D = naive_dc_matrixmultiply(c, f) + naive_dc_matrixmultiply(d, h)

    result = np.zeros((n, n))

    result[:m, :m] = A
    result[:m, m:] = B
    result[m:, :m] = C
    result[m:, m:] = D

    return result


def test_naive_dc_matrixmultiply(n=128):
    x = np.arange(1, n**2 + 1).reshape(n, n)
    y = np.arange(1, n**2 + 1).reshape(n, n) + n**2
    return naive_dc_matrixmultiply(x, y)


def test_strassen_matrixmultiply(n=128):
    x = np.arange(1, n**2 + 1).reshape(n, n)
    y = np.arange(1, n**2 + 1).reshape(n, n) + n**2
    return strassen_matrixmultiply(x, y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
