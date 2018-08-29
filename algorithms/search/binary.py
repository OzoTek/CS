# O(log N)

import math


def rec_search(arr, n, lo, hi):
    if len(arr) == 0 or lo > hi:
        return -1
    low = 0 if lo == None else lo
    high = len(arr) - 1 if hi == None else hi
    idx = math.floor(low + (high - low) / 2)
    if n == arr[idx]:
        return idx
    elif n > arr[idx]:
        return rec_search(arr, n, idx + 1, high)
    else:
        return rec_search(arr, n, low, idx - 1)


def search(arr, n):
    return rec_search(arr, n, 0, len(arr) - 1)


n = 2
arr = list([-1000, 1, 2, 3, 4, 5, 1000])
print(f'idx of "{str(n)}" in "{str(arr)}": "{search(arr, n)}"')
