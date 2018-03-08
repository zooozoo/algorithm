def number_generator(x, n):
    # 함수를 완성하세요
    l = []
    for i in range(n):
        item = x * (i +1)
        l.append(item)
    return l

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(2,5))
