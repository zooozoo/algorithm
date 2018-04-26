num = [12, 11, 38, 54, 47, 47, 53, 80, 42, 18]


def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)


# 최소공배수 구하는 함수
def lcm(a, b):
    gcd_value = gcd(a, b)
    if gcd_value == 0:
        return 0
    return a * b // gcd(a, b)


for i in range(len(num)-1):
    a = num.pop(0)
    b = num.pop(0)
    num.append(lcm(a, b))


print(num)