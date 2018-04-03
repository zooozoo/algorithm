s = "맛토마토있어"
length = 0


for i in range(3, len(s)+1):
    # print('i ---------------------- :', i)
    for a in range(len(s)-i+1):
        part = s[a:a + i]
        rev_part = part[::-1]
        if part == rev_part:
            if length < len(part):
                length = len(part)
        # print(s[a:a+i])
        # print(rev_part)
        # print(f'a = {a}, i+a = {i+a}')




def longest_palindrom(s):
    # 함수를 완성하세요
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))


# 아래는 테스트로 출력해 보기 위한 코드입니다.

