# time O(N log N)
# space O(log N) instead of classic O(N):
#   1.  tail call elimination
#   2.  minimizing of the recursive stack (recur only through the smallest partition,
#       and iterate over the other)

import random

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[hi] = pivot, arr[i + 1]
    return i + 1

def quickSort(arr, lo, hi):
    while lo < hi:
        pi = partition(arr, lo, hi)

        if pi - lo < hi - pi:
            quickSort(arr, lo, pi - 1)
            lo = pi + 1
        else:
            quickSort(arr, pi + 1, hi)
            hi = pi - 1

def sort(arr):
    random.shuffle(arr)
    quickSort(arr, 0, len(arr) - 1)

arr = list([2, 4, 3, 1, 5, 2, 5, 8, 8, 8, 9, 3, 124, -214e23, -4, 98931e234])
print(f'before {str(arr)}')
sort(arr)
print(f'after {str(arr)}')
