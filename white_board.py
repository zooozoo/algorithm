def toWeirdCase(s):
    # 함수를 완성하세요
    word_list = s.split()
    result_list = []
    for word in word_list:
        nw = ''
        for w_sequence in range(len(word)):
            if w_sequence == 0 or w_sequence % 2 == 0:
                nw += word[w_sequence].capitalize()
            else:
                nw += word[w_sequence].lower()
        result_list.append(nw)
    return ' '.join(result_list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));