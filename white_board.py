def fibonacci(num):
    if num >= 2:
        cicle = 0
        first = 0
        second = 1
        while True:
            answer = first + second
            first = second
            second = answer
            cicle += 1
            if cicle == (num - 1):
                return answer
    elif num == 0:
        answer = num
        return answer
    elif num == 1:
        answer = num
        return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(5))