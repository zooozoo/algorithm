def rotLeft(a, d):
    left = a[:d]
    right = a[d:]
    return right+left

print(rotLeft([1,2,3,4,5], 4))