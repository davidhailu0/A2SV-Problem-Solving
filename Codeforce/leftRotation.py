def rotateLeft(d, arr):
    d = d % len(arr)
    return arr[d:] + arr[:d]


print(rotateLeft(2, [1, 2, 3, 4, 5])) 