def jumpCase(num):
    two = num // 2
    answer = 1
    for t in range(two):
        total_element = (num - 2 * (t + 1)) + (t + 1)
        if (num - 2 * (t + 1)) == 0:
            answer += 1
            continue
        total_element_factorial = 1
        a = 1
        b = 1
        for i in range(total_element):
            total_element_factorial *= (i + 1)
        for i in range((num - 2 * (t + 1))):
            a *= (i + 1)
        for i in range(t + 1):
            b *= (i + 1)
        answer += total_element_factorial / (a * b)

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.

def jumpCase1(num):
    a = 1
    b = 1
    while num > 0:
        num = num - 1
        a, b = b, a + b

    return a


print('내꺼', jumpCase(7))
print('new', jumpCase1(7))
