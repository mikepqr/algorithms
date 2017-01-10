def even(x):
    if x % 2 == 0:
        return True


def double(x):
    return 2 * x


def fmult(x, y):
    if y == 0:
        return 0
    z = fmult(x, y//2)
    if even(y):
        return double(z)
    else:
        return x + double(z)


def div(x, y):
    if x == 0:
        return 0, 0
    q, r = div(x//2, y)
    q = double(q)
    r = double(r)
    if not even(x):
        r += 1
    if r >= y:
        r -= y
        q += 1
    return q, r
