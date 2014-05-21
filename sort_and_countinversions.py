def sort_and_countinversions(s):
    '''
    Mergesort and count the inversions in the list of numbers s

    Divide-and-conquer that recursively mergesorts each half of the list, and
    then combines the the results with merge_and_countsplitinversions(), which
    also counts inversions.

    >>> sort_and_countinversions([1, 3, 5, 2, 4, 6])
    ([1, 2, 3, 4, 5, 6], 3)
    '''
    n = len(s)
    if n == 1:
        return (s, 0)
    m = n//2
    s1 = s[:m]
    s2 = s[m:]

    (s1, x) = sort_and_countinversions(s1)
    (s2, y) = sort_and_countinversions(s2)
    (s, z) = merge_and_countsplitinversions(s1, s2)
    return (s, x + y + z)


def merge_and_countsplitinversions(s1, s2):
    '''
    Merge two lists of numbers s1 and s2, while counting split inversions.

    Walks through each list using counters j and k. Compares s1[j] and s2[k].
    If s1[j] is smaller, it is appended to the output list and j += 1. If s2[k]
    is smaller it is appended to the output list and k += 1. When the end of
    either list is reached, the remainder of the other is appended.

    A split inversion occurs whenever s2[k] is selected before s1[j]. Such a
    selection implies that there are s1[j:] split inversions associated with
    s2[k].
    '''
    s = []
    count = 0
    j, k = 0, 0
    while j < len(s1) and k < len(s2):
        if s1[j] <= s2[k]:
            s.append(s1[j])
            j += 1
        else:
            s.append(s2[k])
            k += 1
            count += len(s1[j:])

    # If nothing remaining of list s1, append s2 to s. Note that this append
    # must be done with += (not .append) because a slice of a list is itself
    # a list.
    if len(s1[j:]) == 0:
        s += s2[k:]
    if len(s2[k:]) == 0:
        s += s1[j:]

    return (s, count)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
