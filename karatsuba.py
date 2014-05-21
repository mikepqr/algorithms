def karatsuba(x, y):
    '''
    Perform Karatsuba multiplication of integers x and y.

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

        xy = (x1 * 10**(2m)) + x2) * (y0 * 10**m + y1)
           = x1*y1 * 10**(2m) + (x1*y2 + x2*y1) * 10**m + x2*y2

    Note: if x or y have an even number of digits n, the optimal choice of m
    (from the point of view of an efficient divide-and-conquer) is n/2, and x1
    and x2 have the same length. If n is odd, the optimal choice of m is
    about n/2, e.g.

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

    nx, ny = len(str(x)), len(str(y))
    n = min(nx, ny)
    if n == 1:
        # Base case
        return x*y
    # Split in half if even (or (n-1)/2 and (n+1)/2 if odd)
    m = n//2

    # Split into two chunks, second of which is of length m. E.g. if x = 12345
    # and m = 2, make use of integer division //.
    #   x1 = 12345//(10**2) = 123
    # Then
    #   x2 = 12345 % (12*(10**2)) = 45
    x1 = x // (10**m)
    x2 = x % (x1*(10**m))
    y1 = y // (10**m)
    y2 = y % (y1*(10**m))

    p1 = karatsuba(x1, y1)
    p2 = karatsuba(x2, y2)
    p3 = karatsuba(x1 + x2, y1 + y2)
    return p1 * 10**(2*m) + (p3 - p2 - p1) * 10**m + p2


def gradeschool_multiply(x, y):
    '''
    Perform 'grade school' multiplication of two integers x and y.

    Identical to Karatsuba multiplication, but without the trick to avoid the
    4th product of the divided numbers.

    >>> gradeschool_multiply(2, 3)
    6
    >>> gradeschool_multiply(1234, 5678)
    7006652
    >>> gradeschool_multiply(1234873409857345, 12348380987450934)
    15248687336191143786500127010230L
    '''
    nx, ny = len(str(x)), len(str(y))
    n = min(nx, ny)
    if n == 1:
        # Base case
        return x*y
    # Split in half if even (or (n-1)/2 and (n+1)/2 if odd)
    m = n//2

    # Split into two chunks, second of which is of length m. E.g. if x = 12345
    # and m = 2, make use of integer division //.
    #   x1 = 12345//(10**2) = 123
    # Then
    #   x2 = 12345 % (12*(10**2)) = 45
    x1 = x // (10**m)
    x2 = x % (x1*(10**m))
    y1 = y // (10**m)
    y2 = y % (y1*(10**m))

    p1 = gradeschool_multiply(x1, y1)
    p2 = gradeschool_multiply(x2, y2)
    p3 = gradeschool_multiply(x1, y2)
    p4 = gradeschool_multiply(x2, y1)
    return p1 * 10**(2*m) + (p3 + p4) * 10**m + p2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
