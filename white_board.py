def water_melon(n):
    # 함수를 완성하세요.
    word = '수박'
    if n % 2 == 0:
        return word*(int(n/2))
    num = int((n-1)/2)
    return (word*num)+word[0]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));