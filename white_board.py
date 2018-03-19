def numPY(s):
    # 함수를 완성하세요
    p = []
    y = []
    for i in s:
        if i.lower() == 'p':
            p.append(i)
        if i.lower() == 'y':
            y.append(i)
    if len(p) == len(y):
        return True
    return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numPY("pPoooyY"))
print(numPY("Pyy"))