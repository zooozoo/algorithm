# 문제
is_pair함수는 문자열 s를 매개변수로 입력받습니다.
s에 괄호가 알맞게 짝지어져 있으면 True를 아니면 False를 리턴하는 함수를 완성하세요.
예를들어 s가 (hello)()면 True이고, )(이면 False입니다.
s가 빈 문자열("")인 경우는 없습니다.

# 새로 알게된 것
다른사람의 답변도 거진 다 비슷했다. 
다만 추천을 많이 받은 답안이 오류가 있는 답안이여서 좀 의외였다. 
다른건 별로 기록해 둬야 할 가치를 못느꼈다.


### 내 풀이
```python
def is_pair(s):
    # 함수를 완성하세요
    count_target = 0
    result = True
    for i in s:
        if i == '(':
            count_target += 1
        if i == ')':
            count_target -= 1
        if count_target < 0:
            result = False
            break
    if count_target != 0:
        result = False
    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))
```
