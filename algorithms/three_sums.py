# O(N^2)
def three_sums(array, target):
    if array[0] > target:
        return None
    n = len(array)
    possible_sums = dict()
    for i in range(0, n - 2):
        a = array[i]
        start = i + 1
        end = n - 1
        while start < end:
            b = array[start]
            c = array[end]
            if a + b + c == target:
                # A simpler boolean variant could just return true here
                # and false as the last statement
                possible_sums[f'{i},{start},{end}'] = [a, b, c]
                if b == array[start + 1]:
                    start += 1
                else:
                    end -= 1
            elif a + b + c > target:
                end -= 1
            else:
                start += 1
    return possible_sums

print(three_sums([-25, -10, -7, -3, 2, 4, 8, 10], -20))
