def longest_palindrom(s):
    # 함수를 완성하세요
    length = 0

    for i in range(3, len(s) + 1):
        for a in range(len(s) - i + 1):
            part = s[a:a + i]
            rev_part = part[::-1]
            if part == rev_part and length < len(part):
                length = len(part)
    return length


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("맛토마토있어"))