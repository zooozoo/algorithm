# 문제

toWeirdCase함수는 문자열 s를 매개변수로 입력받습니다.
문자열 s에 각 단어의 짝수번째 인덱스 문자는 대문자로, 홀수번째 인덱스 문자는 소문자로 바꾼 문자열을 리턴하도록 함수를 완성하세요.
예를 들어 s가 try hello world라면 첫 번째 단어는 TrY, 두 번째 단어는 HeLlO, 세 번째 단어는 WoRlD로 바꿔 TrY HeLlO WoRlD를 리턴하면 됩니다.

주의 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단합니다.

# 새로 알게된 것
`map()`메서드와 `lambda`를 활용해서 한줄로 해결한 풀이가 있긴 했는데 좋아보이진 않았다.
그런식으로 풀이하는게 함수의 기능을 익히는 것 말고 더 좋은점이 있나 모르겠다..

`enumerate()`메서드는 평소에 잘 사용하지는 않았는데 필요할 때 유용하게 사용할 수 있을 것 같아서 
관련 내용을 포스팅한 블로그를 기록해 둔다.
[https://wayhome25.github.io/python/2017/02/24/py-07-for-loop/](https://wayhome25.github.io/python/2017/02/24/py-07-for-loop/)


### 내 풀이
```python
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
```

enumerate의 예
### 다른 풀이1
```python
>>> for i, name in enumerate(['body', 'foo', 'bar']):
...     print(i, name)
...
0 body
1 foo
2 bar
```
