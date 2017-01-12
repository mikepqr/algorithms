import arithmetic


def twoprimes(p=None, q=None, n=100):
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


def keypair(p=None, q=None, n=100):
    '''
    Return a valid RSA public (N, e) and private (N, d) keypair.

    If p and/or q are set they are used as the primes to generate the keys.
    Otherwise primes up to n bits long are randomly generated.
    '''
    p, q = twoprimes(p=p, q=q, n=n)
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
    if x >= N:
        raise ValueError('Message x={} too large for key N={}'.format(x, N))
    return arithmetic.modexp(x, e, N)


def decode(x, private):
    N, d = private
    return arithmetic.modexp(x, d, N)
