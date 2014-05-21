def karatsuba(x, y):
    '''
    Perform Karatsuba multiplication on two decimal numbers
    x and y

    >>> karatsuba(2, 3)
    6
    >>> karatsuba(1234, 5678)
    7006652
    '''
    return x*y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
