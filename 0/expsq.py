import operator
import functools


def standingbits(n):
    '''
    Return a list containing the offsets of the non-zero bits of int n.

    >>> standingbits(12) # 0b1100
    [3, 4]
    '''
    # 12 = 0b1100 -> [0, 0, 1, 1]
    # For each bit from first to length of the number in binary
    # - shift the binary number right by that many bits, 1100 >> 2 = 0011
    # - & that with 0001, which yields 0 if the bit is 0, 1 if 1
    bits = [(n >> bit) & 1 for bit in range(n.bit_length())]

    # Return corresponding numbers, accounting for fact that 0th element of
    # bits corresponds to 1, 1st element = 2, etc.
    return [i + 1 for i, v in enumerate(bits) if v]


def expsq(x, n):
    '''Return x^n using exponentiation by squaring.'''
    if n == 0:
        return 1

    # Make a list containing x^1, x^2, x^4 .. x^leading_bit
    leading_bit = n.bit_length()
    allsquares = [x]
    for i in range(leading_bit):
        allsquares.append(allsquares[-1] * allsquares[-1])

    # Pluck out elements of list that are standing bits of n. e.g. for n=25
    # this gives [x^16, x^8, x^1]
    squares = [allsquares[i-1] for i in (standingbits(n))]

    return functools.reduce(operator.mul, squares)
