def nextSqure(n):
    result = 'no'
    for i in range(n):
        if n // (i + 1) == (i + 1):
            result = ((i + 1) + 1) ** 2
    return result
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(3)))