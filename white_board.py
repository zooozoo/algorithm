def Jaden_Case(s):
    # 함수를 완성하세요
    ns = ''
    for i in s.split():
        ns += i.title() + ' '
    return ns.strip()


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))