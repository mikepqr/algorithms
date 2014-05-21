def karatsuba(x, y):
    '''
    Perform Karatsuba multiplication on two positive integers x and y.

    To multiply x = 1234 and y = 5678, we first split these numbers into x1 =
    12, x2 = 34, y1 = 56, y2 = 78. In terms of x1 and x2, x = x1 * 100 + x2.
    Generally, x = x1 * 10**(m2/2) + x2, where m2 is the number of trailing
    zeros to pad x1 with (i.e. the length m2 of the number x2). Then

        xy = (x1 * 10**m2/2) + x2) * (y0 * 10**(m2/2) + y1)
           = x1*y1 * 10**m2 + (x1*y2 + x2*y1) * 10**(m2/2) + x2*y2

    Note: if x or y have an odd number of digits m, the optimal division for a
    divide-and-conquer approach is m1 = (m+1)/2 and m2 = (m-1)/2

    The Karatsuba trick is to note that the x1*x2 + x2*y1 term can be written
    in terms of two products already computed for the other two terms and only
    one new product:

        x1 y2 + x2 y1 = (x1 + x2)(y1 + y2) - x1 y1 - x2 y2

    This observation reduces the number of products that must be computed from
    4 to 3.

    The algorithm calls itself recursively until it encounters the base case,
    in which the longest of the two numbers it is passed is one digit long.

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
