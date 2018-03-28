def collatz(num):
    test_number = num
    answer = 0

    while answer < 500:
        if test_number == 1:
            break
        answer += 1
        if test_number % 2 == 0:
            test_number = test_number / 2
        else:
            test_number = (test_number * 3) + 1
    else:
        answer = -1

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))