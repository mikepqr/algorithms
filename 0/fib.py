import expsq
import functools


class matrix(object):
    '''Trivial 2x2 matrix class implementing multiplication only.'''

    def __init__(self, a, b, c, d):
        # X = [[a b]
        #      [c d]]
        self.values = [a, b, c, d]

    def __repr__(self):
        return "{}({}, {}, {}, {})".format(self.__class__.__name__,
                                           *self.values)

    def __mul__(self, other):
        a = self.values[0] * other.values[0] + self.values[1] * other.values[2]
        b = self.values[0] * other.values[1] + self.values[1] * other.values[3]
        c = self.values[2] * other.values[0] + self.values[3] * other.values[2]
        d = self.values[2] * other.values[1] + self.values[3] * other.values[3]
        return matrix(a, b, c, d)


# http://mike.place/2016/memoization/
@functools.lru_cache()
def fib1(n):
    '''Return the nth Fibonnaci number using recursion and memoization.'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib3(n):
    '''Return the nth Fibonnaci number using matrix exponentiation.'''
    if n == 0:
        return 0
    if n == 1:
        return 1

    x = matrix(0, 1, 1, 1)
    xn = expsq.expsq(x, n)
    return xn.values[1]
