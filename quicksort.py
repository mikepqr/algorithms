def choosepivot_first(A):
    return 0


def choosepivot_last(A):
    return len(A) - 1


def choosepivot_median(A):
    a = A[0]
    b = A[len(A) - 1]
    c = A[(len(A) - 1)//2]
    if a <= b <= c or c <= b <= a:
        return len(A) - 1
    elif b <= a <= c or c <= a <= b:
        return 0
    else:
        return (len(A) - 1)//2


def partition(B, p):
    # Move pivot to beginning of array
    B[0], B[p] = B[p], B[0]
    n = len(B)
    i = 1
    for j in range(1, n):
        if B[j] < B[0]:
            B[i], B[j] = B[j], B[i]
            i += 1
    return (B[1:i], B[i:])


def quicksort(A, comp=0):
    '''
    >>> quicksort([3, 8, 2, 5, 1, 4, 7, 6])
    ([1, 2, 3, 4, 5, 6, 7, 8], 25)
    '''
    if len(A) <= 1:
        return (A, comp)
    else:
        comp += len(A) - 1
        p = choosepivot_first(A)
        p_value = A[p]
        (A1, A2) = partition(A, p)
        A1, comp = quicksort(A1, comp=comp)
        A2, comp = quicksort(A2, comp=comp)
        return (A1 + [p_value] + A2, comp)


def test_quicksort():
    import mergesort
    for n in [10]:
        f = open("quicksort_tests/" + str(n) + ".txt", "r")
        A = [int(i) for i in f]
        A, comp = quicksort(A)
        assert mergesort.mergesort(A) == A
        print comp


if __name__ == "__main__":
    import doctest
    doctest.testmod()
