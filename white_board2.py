def number_generator(x, n):
    return [x * (i + 1) for i in range(n)]

print(number_generator(2, 5))