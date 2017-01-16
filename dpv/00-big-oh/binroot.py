def binsearch(func, x1=0, x2=1, tol=1e-3):
    '''
    Returns x where func(x) changes being truthy to falsey.

    Uses binary search. The solution must lie in the interval (x1, x2), i.e.
    func(x1) and func(x2) must return values of opposite truthiness.
    '''
    while x2 - x1 > tol:
        xtry = x1 + (x2 - x1)/2.
        if bool(func(xtry)) == bool(func(x1)):
            x1, x2 = xtry, x2
        else:
            x1, x2 = x1, xtry

    return x1


def binroot(func, x1=0, x2=1, **kwargs):
    '''Returns the root of x in the interval (x1, x2).'''
    return binsearch(lambda x: True if func(x) > 0 else False,
                     x1, x2, **kwargs)
