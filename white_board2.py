def toWeirdCase(s):
    # 함수를 완성하세요
    seq =0
    answer = ''
    for a in s:
        if a == ' ':
            seq = 0
            answer += ' '
            continue
        elif seq == 0 or seq % 2 == 0:
            answer += a.capitalize()
        else:
            answer += a.lower()
        seq += 1
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));