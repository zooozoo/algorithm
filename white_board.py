def is_pair(s):
    # 함수를 완성하세요
    count_target = 0
    result = True
    for i in s:
        if i == '(':
            count_target += 1
        if i == ')':
            count_target -= 1
        if count_target < 0:
            result = False
            break
    if count_target != 0:
        result = False
    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))