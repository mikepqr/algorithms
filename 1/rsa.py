import arithmetic


def tworandomprimes(n=100):
    p = arithmetic.randomprime(n)
    q = arithmetic.randomprime(n)
    while p == q:
        q = arithmetic.randomprime(n)
    return p, q


def keypair(n=100):
    p, q = tworandomprimes(n=n)
    pq = arithmetic.mult(p, q)
    p1q1 = arithmetic.mult(p - 1, q - 1)

    while True:
        e = arithmetic.randomprime(4)
        try:
            d = arithmetic.multinv(e, p1q1)
        except ValueError:
            pass
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
