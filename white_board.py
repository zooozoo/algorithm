def alpha_string46(s):
    if (len(s) == 4) or (len(s) == 6):
        try:
            int(s)
            return True
        except:
            return False
    return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("4u012") )




# 조건1 - 받은 문자열 s의 길이가 4혹은 6
# 조건2 - 문자열이 오직 숫자로만 이루어져있는지