import operator
import functools
import itertools as it


def iterate(f, x):
    '''Yield the sequence [x, f(x), f(f(x)), f(f(f(x)))...].'''
    while True:
        yield x
        x = f(x)


def standingbits(n):
    '''
    Return a list containing the offsets of the non-zero bits of int n.

    >>> standingbits(12) # 0b1100 = 2^3 + 2^2
    [2, 3]
    >>> standingbits(25) # 0b11001 = 2^4 + 2^3 + 2^0
    [0, 3, 4]
    '''
    # 12 = 0b1100 -> [0, 0, 1, 1]
    # 25 = 0b11001 -> [1, 0, 0, 1, 1]
    # For each bit from first to length of the number in binary
    # - shift the number right by that many bits, e.g. 1100 >> 2 = 0011
    # - & the result with 1, which yields 0 if the rightmost bit is 0, 1 if 1
    bits = [(n >> offset) & 1 for offset in range(n.bit_length())]

    # Return locations of 1s in bits
    return [i for i, b in enumerate(bits) if b]


def expsq(x, n):
    '''Return x^n using exponentiation by squaring.'''
    if n == 0:
        return 1

    # Make a iterator whose ith element is x^(2^i)
    # e.g. for n=25 this gives [x^1, x^2, x^4, x^8, x^16]
    allsquares = it.islice(iterate(lambda a: a*a, x), n.bit_length())

    # Pluck out elements of list that are standing bits of n.
    # e.g. for n=25 this gives [x^1, x^8, x^16]
    squares = (s for i, s in enumerate(allsquares) if i in standingbits(n))

    return functools.reduce(operator.mul, squares)
