def splitnums(x, y):
    '''
    Split two numbers.

    Returns xl, xr, yl, yr, n such that

        (xl * 2^n) + xr == x
        (yl * 2^n) + yr == y

    n is chosen to be half the number of bits in the smaller number.
    '''
    if x < 2 or y < 2:
        raise ValueError('Both x and y must be at least 2 bits long')
    sx, sy = bin(x)[2:], bin(y)[2:]
    n = min(len(sx), len(sy)) >> 1
    return (int(sx[0:-n], 2), int(sx[-n:], 2),
            int(sy[0:-n], 2), int(sy[-n:], 2), n)


def multnonneg(x, y):
    '''
    Return x * y using Karatsuba divide-and-conquer multiplication.

    x and y must be non-negative.
    '''
    if x < 0 or y < 0:
        raise ValueError("x and y must be positive.")
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x

    xl, xr, yl, yr, n = splitnums(x, y)

    p1 = multnonneg(xl, yl)
    p2 = multnonneg(xr, yr)
    p3 = multnonneg(xl + xr, yl + yr)

    return ((p1 << (n << 1)) +
            ((p3 - p1 - p2) << n) +
            p2)


def mult(x, y):
    '''Return x * y using Karatsuba divide-and-conquer multiplication.'''
    if (x < 0) == (y < 0):
        return multnonneg(max(x, -x), max(y, -y))
    else:
        return -multnonneg(max(x, -x), max(y, -y))
