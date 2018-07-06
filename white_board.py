def solve(a, b):
    a_score= 0
    b_score = 0
    for i in range(3):
        if a[i] > b[i]:
            a += 1
        elif a[i] < b[i]:
            b += 1
    return [a_score, b_score]


a = [5, 6, 7]
b = [3, 6, 10]

for i, j in zip(a, b):
    print(i, j)