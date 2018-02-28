def no_continuous(s):
    l = list(s)
    nl = []
    if l:
        first = l.pop(0)
        nl.append(first)
        for n in range(len(l)):
            item = l.pop(0)
            if item == nl[-1]:
                pass
            else:
                nl.append(item)
        return nl
    else:
        return nl

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "111333444888822222233333" ))

