def mergesort(s):
    '''
    Mergesort the list of numbers s

    Divide-and-conquer that recursively mergesorts each half of the list, and
    then combines the the results with merge().

    >>> mergesort([5, 4, 1, 6, 2, 3, 9, 7])
    [1, 2, 3, 4, 5, 6, 7, 9]

    >>> mergesort([3, 2, 4, 2, 1])
    [1, 2, 2, 3, 4]
    '''
    n = len(s)
    if n == 1:
        return s
    m = n//2
    s1 = s[:m]
    s2 = s[m:]

    s1 = mergesort(s1)
    s2 = mergesort(s2)
    return merge(s1, s2)


def merge(s1, s2):
    '''
    Merge two lists of numbers s1 and s2.

    Walks through each list using counters j and k. Compares s1[j] and s2[k].
    If s1[j] is smaller, it is appended to the output list and j += 1. If s2[k]
    is smaller it is appended to the output list and k += 1. When the end of
    either list is reached, the remainder of the other is appended.
    '''
    s = []
    j, k = 0, 0
    while j < len(s1) and k < len(s2):
        if s1[j] <= s2[k]:
            s.append(s1[j])
            j += 1
        else:
            s.append(s2[k])
            k += 1

    # If nothing remaining of list s1, append s2 to s. Note that this append
    # must be done with += (not .append) because a slice of a list is itself
    # a list.
    if len(s1[j:]) == 0:
        s += s2[k:]
    if len(s2[k:]) == 0:
        s += s1[j:]

    return s

if __name__ == "__main__":
    import doctest
    doctest.testmod()
