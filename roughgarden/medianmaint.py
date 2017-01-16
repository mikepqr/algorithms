import heapq


def rebalanceHeaps(hlow, hhigh):
    '''
    Rebalance distribution of elements in hlow (max-heap) and hhigh (min-heap)
    to ensure len(hlow) = len(hhigh) +/- 1.
    '''
    unbalance = len(hlow) - len(hhigh)
    if unbalance == 2:
        # move one element to hhigh
        move = -1 * heapq.heappop(hlow)
        heapq.heappush(hhigh, move)
    if unbalance == -2:
        # move one element to hlow
        move = heapq.heappop(hhigh)
        heapq.heappush(hlow, -1 * move)


def medianmaint(test=None):
    '''
    Computes a runnning median of a list of numbers as those numbers are read
    in. Uses two heaps hlow (max-heap) and hhigh (min-heap). Elements are added
    to each queue in such a way as the maximum value in hlow or the minimum of
    hhigh is guaranteed to be the current median.

    In order to ensure this:

    (1) each new element must be added to hlow if < largest element in hlow, or
    to hhigh if > smallest element in hmax (and, arbitrarily, to hlow if
    between these two).

    (2) the two heaps must be rebalanced in order to ensure that they are the
    same length (or within one element of each other).

    Note: Python heapq supports only min-heap. A max-heap is implemented here
    by multiplying numbers by -1 before pushing them onto the heap and
    multiplying them by -1 after popping them off.

    Note: if the number of elements n is even then median is here defined to be
    the n/2th element. If odd then (as usual) it is the (n+1)/2th element.

    >>> medianmaint(test=1)
    54
    >>> medianmaint(test=2)
    55
    >>> medianmaint(test=3)
    148
    >>> medianmaint(test=4)
    82
    '''
    if test:
        file = 'medianmaint_tests/medianmaint_tc' + str(test) + '.txt'
    else:
        file = 'medianmaint_tests/Median.txt'

    hlow = []
    hhigh = []
    medians = []

    with open(file, 'r') as lines:
        # Put the first two on hlow and hhigh and record the medians manually
        a = int(lines.readline())
        b = int(lines.readline())

        medians.append(a)
        if a <= b:
            heapq.heappush(hlow, -1 * a)
            heapq.heappush(hhigh, b)
            medians.append(a)
        if a > b:
            heapq.heappush(hlow, -1 * b)
            heapq.heappush(hhigh, a)
            medians.append(b)

        i = 2

        for xi in lines:
            xi = int(xi)

            # Read hhighmin and hlowmax off the heaps (and restore heaps)
            hhighmin = heapq.heappop(hhigh)
            heapq.heappush(hhigh, hhighmin)
            hlowmax = -1 * heapq.heappop(hlow)
            heapq.heappush(hlow, -1 * hlowmax)

            # Put xi on appropriate heap
            if xi > hhighmin:
                heapq.heappush(hhigh, xi)
            if xi < hlowmax:
                heapq.heappush(hlow, -1 * xi)
            if hlowmax < xi < hhighmin:
                heapq.heappush(hlow, -1 * xi)

            # Rebalance heaps to ensure they are the same length
            rebalanceHeaps(hlow, hhigh)

            # Record median (either hlowmax or hhighmin).
            i += 1
            seek = (i+1)//2
            if seek == len(hlow):
                median = -1 * heapq.heappop(hlow)
                heapq.heappush(hlow, -1 * median)
                medians.append(median)
            elif seek == len(hlow) + 1:
                median = heapq.heappop(hhigh)
                heapq.heappush(hhigh, median)
                medians.append(median)
            else:
                print i, seek, hlow, hhigh

    # Return sum(medians) % 10000 as requested in problem
    return sum(medians) % 10000


if __name__ == "__main__":
    import doctest
    doctest.testmod()
