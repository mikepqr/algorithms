import binroot
import fib


def checkc(c, nmax=1000):
    '''
    Return True if the nth Fibonnaci number <= 2**(c*n) for all n < nmax.
    '''
    comparisons = (fib.fib3(n) <= 2**(c*n)
                   for n in range(nmax))
    return all(comparisons)


def ex03b(c=0.8):
    if checkc(c):
        print("c={} is a solution to 0.3(b)".format(c))
    else:
        print("c={} is not a solution to 0.3(b)".format(c))


def ex03c():
    return binroot.binsearch(checkc)
