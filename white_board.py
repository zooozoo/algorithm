def sum_digit(number):
    num = number
    place_value = len(str(num))
    value = 0
    for i in reversed(range(place_value)):
        if i is 0:
            value += num
            return value
        value += num // (10 ** i)
        num = num % (10 ** i)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));