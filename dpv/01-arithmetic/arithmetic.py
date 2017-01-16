'''
Implement basic arithmetic operations using the following bit-based primitives:

 - test x for even
 - double x
 - floor divide x by 2, i.e. halve

and integer addition/subtraction, comparison of two integers, and test for
equality to zero.
'''
import random


def even(x):
    return False if x & 1 else True


def double(x):
    return x << 1


def halve(x):
    return x >> 1


def multpos(x, y):
    '''Multiply two positive integers using the French method.'''
    if y == 0:
        return 0
    z = multpos(x, halve(y))
    if even(y):
        return double(z)
    else:
        return x + double(z)


def mult(x, y):
    '''Multiply two integers.'''
    if x < 0 and y >= 0:
        return -multpos(-x, y)
    elif x >= 0 and y < 0:
        return -multpos(x, -y)
    elif x < 0 and y < 0:
        return multpos(-x, -y)
    else:
        return multpos(x, y)


def square(x):
    return mult(x, x)


def divpos(x, y):
    '''Divide two positive integers.'''
    if x == 0:
        return 0, 0
    q, r = divpos(halve(x), y)
    q = double(q)
    r = double(r)
    if not even(x):
        r += 1
    if r >= y:
        r -= y
        q += 1
    return q, r


def mod(x, N):
    '''Return x mod N.'''
    if x < 0:
        return N - divpos(-x, N)[1]
    else:
        return divpos(x, N)[1]


def modexp(x, y, N=0):
    '''Return x^y mod N.'''
    if y == 0:
        return 1
    z = modexp(x, halve(y), N)
    if even(y):
        return mod(square(z), N)
    else:
        return mod(mult(x, square(z)), N)


def gcd(a, b):
    '''Return gcd(a, b) using Euclid's algorithm.'''
    if b == 0:
        return a
    else:
        return gcd(b, mod(a, b))


def quotient(x, N):
    '''Return x//N'''
    return divpos(x, N)[0]


def egcd(a, b):
    '''Returns x, y, d such that d = gcd(a, b) and ax + by = d.'''
    if b == 0:
        return 1, 0, a
    xprime, yprime, dprime = egcd(b, mod(a, b))
    x = yprime
    y = xprime - mult(quotient(a, b), yprime)
    d = dprime
    return x, y, d


def multinv(a, N):
    '''
    Returns the multiplicative inverse of a modulo N, i.e. x such that ax ≡ 1
    (mod N). This does not exist if the greatest common divisor of a and N ≠ 1,
    i.e. if a and N are not relatively prime.
    '''
    x, y, d = egcd(a, N)
    if d == 1:
        return mod(x, N)
    else:
        raise ValueError('a and N are not relatively prime.')


def prime(N, k=100, a=None):
    '''
    Returns True if a number is probably prime, False if it is definitely not.

    If a is none this uses k applications of Fermat's Little Theorem.
    Probability of failure (i.e. probability returns True if not a prime) is
    < 1/2^k.

    If a is an iterable, it performs the test for those values of a.
    '''
    def fermat_test(a):
        return modexp(a, N-1, N) == 1
    if a:
        a = [ai for ai in a if ai < N]
    if a is None:
        if k >= N:
            k = N - 1
        a = random.sample(range(1, N), k)
    return all(fermat_test(ai) for ai in a)


def randomprime(n):
    '''
    Returns a random prime that is no more than n bits long.
    '''
    Nmax = modexp(2, n) - 1
    while True:
        N = random.randint(2, Nmax)
        if prime(N, a=(2, 3, 5)):
            return N


def lcm(a, b):
    '''Return the lowest common multiple of integers a and b.'''
    return quotient(mult(a, b), gcd(a, b))
