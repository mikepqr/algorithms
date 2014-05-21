def karatsuba(x, y):
    '''
    Perform Karatsuba multiplication on two decimal numbers
    x and y

    >>> karatsuba(2, 3)
    6
    >>> karatsuba(1234, 5678)
    7006652
    >>> karatsuba(12345, 5678)
    70094910
    '''

    xs = str(x)
    ys = str(y)
    nx, ny = len(xs), len(ys)
    n = max(nx, ny)
    if n == 1:
        return x*y

    if nx < n:
        xs = '0' * (n - nx) + xs
    if ny < n:
        ys = '0' * (n - ny) + xs

    m0 = (n + 1)/2
    m1 = n/2

    x1 = int(xs[0:m0])
    x2 = int(xs[m0:])
    y1 = int(ys[0:m0])
    y2 = int(ys[m0:])

    p1 = karatsuba(x1, y1)
    p2 = karatsuba(x2, y2)
    p3 = karatsuba(x1 + x2, y1 + y2)
    result = p1 * 10**(2*m1) + (p3 - p2 - p1) * 10**m1 + p2
    # print x1, x2, y1, y2, p1, p2, p3, result
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
