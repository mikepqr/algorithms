import arithmetic


def twoprimes(n=100, p=None, q=None):
    '''
    Returns two different primes up to n bits long.

    If p (or q) is set then one of the numbers returned is p (or q).
    '''
    if (p is not None) and (q is not None):
        return p, q

    if p is None:
        p = arithmetic.randomprime(n)
        while p == q:
            p = arithmetic.randomprime(n)

    if q is None:
        q = arithmetic.randomprime(n)
        while q == p:
            q = arithmetic.randomprime(n)

    return p, q


def keypair(n=100, p=None, q=None):
    '''
    Return a valid RSA public (N, e) and private (N, d) keypair.

    If p and/or q are set they are used as the primes to generate the keys.
    Otherwise primes up to n bits long are randomly generated.
    '''
    p, q = twoprimes(n=n, p=p, q=q)
    pq = arithmetic.mult(p, q)
    p1q1 = arithmetic.mult(p - 1, q - 1)

    e = 2
    while True:
        try:
            d = arithmetic.multinv(e, p1q1)
        except ValueError:
            e += 1
        else:
            break

    public = (pq, e)
    private = (pq, d)
    return public, private


def encode(x, public):
    N, e = public
    return arithmetic.modexp(x, e, N)


def decode(x, private):
    N, d = private
    return arithmetic.modexp(x, d, N)
