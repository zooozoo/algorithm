def Harshad(n):
    # n은 하샤드 수 인가요?
    number_to_string = str(n)
    added = 0
    for i in number_to_string:
        added += int(i)
    if n % added == 0:
        return True
    return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(11))