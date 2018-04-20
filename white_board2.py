num = 5
# 올바른 결과값 233
two = num // 2
answer = 1
for t in range(two):
    total_element = (num - 2 * (t + 1)) + (t + 1)
    print(f'total_element {total_element}')
    print(f'a의 개수 {(num-2*(t+1))}, b의 개수{t+1}')
    # 2만 있는경우 (1이 하나도 없는경우)
    if (num - 2 * (t + 1)) == 0:
        answer += 1
        continue
    total_element_number = 1
    a = 1
    b = 1
    # 이번 턴에 분모로 쓰일 전체 자릿수의 갯수
    for i in range(total_element):
        total_element_number *= (i + 1)
    # 이번 턴에 분자로 쓰일 1의 개수의 팩토리얼
    print(f'total_element_number 분자 {total_element_number}')
    for i in range((num - 2 * (t + 1))):
        a *= (i + 1)
    # 이번 턴에 분자로 쓰일 2의 개수의 팩토리얼
    for i in range(t + 1):
        b *= (i + 1)
    answer += total_element_number // (a * b)
    print(f'분모: 팩토리얼a {a}, 팩토리얼b {b}')
    print(f'total_element_number/(a*b) {total_element_number}/{a*b} = {total_element_number/(a*b)}')
    print(f'answer {answer} \n\n')

print(answer)


# for i in range(2, 4):
#     print(i)
