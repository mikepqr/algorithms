def choosepivot_first(A):
    '''
    Use first element as pivot.
    '''
    return 0


def choosepivot_last(A):
    '''
    Use last element as pivot.
    '''
    return len(A) - 1


def choosepivot_median(A):
    '''
    Use median of [first, last, middle] elements as pivot.

    Note: if A is even length, rounds *down* for middle element index
    '''
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
    '''
    Given an array B and the index of a pivot element p, partition the array,
    i.e. sort it such that all elements smaller than the pivot come before all
    elements larger than the pivot, and the pivot comes between the two groups.
    '''
    # Move pivot to beginning of array
    B[0], B[p] = B[p], B[0]
    n = len(B)
    i = 1

    # Walk through array, swapping when necessary
    for j in range(1, n):
        if B[j] < B[0]:
            B[i], B[j] = B[j], B[i]
            i += 1

    # Swap pivot at B[0] with element at end of lesser partition to ensure
    # array is [lesser, pivot, greater]
    B[0], B[i-1] = B[i-1], B[0]
    return B, i-1


def quicksort(A, comp=0):
    '''
    Returns quicksorted array A and number of primitive comparisons made in
    partition functions.
    >>> quicksort([3, 8, 2, 5, 1, 4, 7, 6])
    ([1, 2, 3, 4, 5, 6, 7, 8], 15)
    '''
    if len(A) <= 1:
        return (A, comp)
    else:
        comp += len(A) - 1
        # p is index of pivot
        p = choosepivot_first(A)
        # Partition a and update p to be new location of pivot
        A, p = partition(A, p)

        # Recursively quicksort lesser and greater partitions
        A1, comp = quicksort(A[:p], comp=comp)
        A2, comp = quicksort(A[p+1:], comp=comp)

        # Stitch together results, with pivot in the middle
        return (A1 + [A[p]] + A2, comp)


def test_quicksort():
    '''
    Answers are:
    size    first   last    median
    10      25      29      21
    100     615     587     518
    1000    10297   10184   8921
    '''
    import mergesort
    for n in [10, 100, 1000]:
        f = open("quicksort_tests/" + str(n) + ".txt", "r")
        A = [int(i) for i in f]
        A, comp = quicksort(A)
        assert mergesort.mergesort(A) == A
        print comp


def exercise_quicksort():
    '''
    Prints solution to algorithms week 2 programming problems (edit quicksort
    to use appropriate pivot selection).
    '''
    import mergesort
    f = open("quicksort_tests/QuickSort.txt", "r")
    A = [int(i) for i in f]
    A, comp = quicksort(A)
    assert mergesort.mergesort(A) == A
    print comp


if __name__ == "__main__":
    import doctest
    doctest.testmod()
