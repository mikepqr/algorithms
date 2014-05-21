def karatsuba(x, y):
    '''
    Perform Karatsuba multiplication on two positive integers x and y.

    The Karatsuba algorithm splits the two numbers to be multiplied into
    leading and trailing parts and expresses the desired product as a
    non-obvious combination of the products of those parts. The products of
    those parts are themselves computed by recursively calling Karatsuba until
    the two numbers to be multiplied are small enough to use basic
    multiplication.

    To multiply x = 1234 and y = 5678, we first divide these numbers in some
    way, e.g. into x1 = 12, x2 = 34, y1 = 56, y2 = 78. In terms of x1 and x2, x
    = x1 * 100 + x2. Generally, x = x1 * 10**(m/2) + x2, where m is the
    number of trailing zeros to pad x1 with (i.e. the length m of the number
    x2). Then

        xy = (x1 * 10**m/2) + x2) * (y0 * 10**(m/2) + y1)
           = x1*y1 * 10**m + (x1*y2 + x2*y1) * 10**(m/2) + x2*y2

    Note: if x or y have an even number of digits n, the optimal choice of m
    (from the point of view of an efficient divide-and-conquer) is n/2, and x1
    and x2 have the same length. If n is odd, the optimal choice of m is
    (n-1)/2. In this case, x1 has length (n+1)/2.

    The Karatsuba trick is to note that the x1*x2 + x2*y1 term above can be
    written in terms of two products already computed for the other two terms
    and only one new product:

        x1 y2 + x2 y1 = (x1 + x2)(y1 + y2) - x1 y1 - x2 y2

    This observation reduces the number of products that must be computed to 3
    from 4 (the "grade school algorithm").

    >>> karatsuba(2, 3)
    6
    >>> karatsuba(1234, 5678)
    7006652
    >>> karatsuba(1234873409857345, 12348380987450934)
    15248687336191143786500127010230L
    '''

    xs = str(x)
    ys = str(y)
    mx, my = len(xs), len(ys)
    m = max(mx, my)
    if m == 1:
        return x*y

    # Pad input to the same length by adding leading zeros
    if mx < m:
        xs = '0' * (m - mx) + xs
    if my < m:
        ys = '0' * (m - my) + ys

    # Split into two chunks of length m1 and m2. // is integer divsion so:
    # m1 = m/2 if n even, (m+1)/2 if odd
    # m2 = m/2 if n even, (m-1)/2 if odd
    m1 = (m + 1)//2
    m2 = m//2
    x1 = int(xs[0:m1])
    x2 = int(xs[m1:])
    y1 = int(ys[0:m1])
    y2 = int(ys[m1:])

    p1 = karatsuba(x1, y1)
    p2 = karatsuba(x2, y2)
    p3 = karatsuba(x1 + x2, y1 + y2)
    result = p1 * 10**(2*m2) + (p3 - p2 - p1) * 10**m2 + p2
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
