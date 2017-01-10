'''
Implement basic arithmetic operations using the following bit-based primitives:

 - test x for even
 - double x
 - floor divide x by 2, i.e. halve

and integer addition/subtraction, comparison of two integers, and test for
equality to zero.
'''


def even(x):
    return False if x & 1 else True


def double(x):
    return x << 1


def halve(x):
    return x >> 1


def mult(x, y):
    if y == 0:
        return 0
    z = mult(x, halve(y))
    if even(y):
        return double(z)
    else:
        return x + double(z)


def square(x):
    return mult(x, x)


def div(x, y):
    if x == 0:
        return 0, 0
    q, r = div(halve(x), y)
    q = double(q)
    r = double(r)
    if not even(x):
        r += 1
    if r >= y:
        r -= y
        q += 1
    return q, r


def mod(x, N):
    '''Return x mod N'''
    return div(x, N)[1]


def modexp(x, y, N=0):
    '''Return x^y mod N'''
    if y == 0:
        return 1
    z = modexp(x, halve(y), N)
    if even(y):
        return mod(square(z), N)
    else:
        return mod(mult(x, square(z)), N)
