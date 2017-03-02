import arithmetic
import sys

cpsize = len(str(sys.maxunicode))  # codepoint size


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


def encode_num(x, public):
    N, e = public
    if x >= N:
        raise ValueError('Message x={} too large for key N={}'.format(x, N))
    return arithmetic.modexp(x, e, N)


def decode_num(x, private):
    N, d = private
    return arithmetic.modexp(x, d, N)


def encode(clear_message, public):
    ords = [ord(m) for m in clear_message]
    ords_str = ''.join(str(o).zfill(cpsize) for o in ords)
    # prepend arbitrary non-zero digit to ensure leading 0s are not lost
    x = int('9' + ords_str)
    return encode_num(x, public)


def decode(encrypted_message, private):
    x = str(decode_num(encrypted_message, private))
    # chunk decoded string into cpsize strings, skipping arbitrary digit
    ords = [int(x[i:i+cpsize]) for i in range(1, len(x), cpsize)]
    return ''.join(chr(o) for o in ords)
