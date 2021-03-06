# 문제
효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)
의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 
효진이가 끝에 도달하는 방법이 몇 가지인지 출력하는 jumpCase 함수를 완성하세요. 예를 들어 4가 입력된다면, 
5를 반환해 주면 됩니다.


# 새로 알게된 것
문제를 해결하기 위해 정석책을 펼쳐봤다. 중복된 순열을 어떻게 계산해 낼지 생각이 안났기 때문이다.
고등학교 때에는 몰랐는데 지금보니 이런 공식을 만들어 낸 사람들이 정말 대단하다는 생각과 동시에 
공식이 아름다워 보였다. 각각의 사람들이 자신의 자리에서 이런 성과들을 쌓아왔기에 지금의 내가 이런 멋진 공식을
보고 있지 않나 하는 생각이 들었다. 
난 공식을 이용해서 문제를 풀었는데 다른 사람들의 풀이를 보니 나와 비슷하게 푼 사람들이 아무도 없었다.
다들 '피보나치 수열'이라는 것을 이용해서 풀었다. 
여기에 피보나치가 적용되는지는 몰랐다. 아마도 1부터 시작해 하나하나 규칙성을 발견해 내기보다는 계산 과정에서의
규칙만 발견해 내려고 했기 때문이 아닐까 싶다.

인터넷에서는 알고리즘 문제해결 전략이라는 책의 내용을 통해 어떻게 접근해야 할 지 방법도 기록해 놓은 것이 있다.
지금 읽고 있는 알고리즘 책을 빨리 읽고 해당 책을 한번 읽어봐야 겠다.

피보나치 수열을 심플하게 구현해놓은 다른사람의 풀이를 기록해 둔다.


### 내 풀이
```python
def jumpCase(num):
    two = num // 2
    answer = 1
    for t in range(two):
        total_element = (num - 2 * (t + 1)) + (t + 1)
        if (num - 2 * (t + 1)) == 0:
            answer += 1
            continue
        total_element_factorial = 1
        a = 1
        b = 1
        for i in range(total_element):
            total_element_factorial *= (i + 1)
        for i in range((num - 2 * (t + 1))):
            a *= (i + 1)
        for i in range(t + 1):
            b *= (i + 1)
        answer += total_element_factorial / (a * b)

    return answer
```

enumerate의 예
### 다른 풀이1
```python
def jumpCase1(num):
    a = 1
    b = 1
    while num > 0:
        num = num - 1
        a, b = b, a + b

    return a
```
