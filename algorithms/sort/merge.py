# O(N log N)

import math

def merge(left, right):
    aux = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            aux.append(left[0])
            del left[0]
        else:
            aux.append(right[0])
            del right[0]

    aux.extend(left)
    aux.extend(right)
    return aux

def sort(arr):
    if len(arr) < 2:
        return arr

    left = sort(arr[0:math.floor(len(arr) / 2)])
    right = sort(arr[math.floor(len(arr) / 2):len(arr)])

    return merge(left, right)

arr = list([2, 4, 3, 1, 5, 2, 5, 8, 8, 8, 9, 3, 124, -214e23, -4, 98931e234])
print(f'before {str(arr)}')
print(f'after {str(sort(arr))}')
