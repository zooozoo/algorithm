def plusMinus(n, arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print(format(positive/n, '.6f'), "\n", format(negative/n, '.6f'),"\n", format(zero/n, '.6f'))

plusMinus(6, [-4, 3, -9, 0, 4, 1])