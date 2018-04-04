# 문제
Jaden_Case함수는 문자열 s을 매개변수로 입력받습니다.
s에 모든 단어의 첫 알파벳이 대문자이고, 그 외의 알파벳은 소문자인 문자열을 리턴하도록 함수를 완성하세요
예를들어 s가 3people unFollowed me for the last week라면 3people Unfollowed Me For The Last Week를 리턴하면 됩니다.

# 새로 알게된 것
이번 문제는 그냥 python의 `title()` 메서드를 알고 있는지 간보는 듯한 문제였다.
그냥 return값에 `title()`메서드를 사용해도 되는데 앞쪽에 공백이 있을경우 오답처리한다.
`strip()`메서드를 추가한다. row나 upper 메서드를 사용할 뿐 다른 답변중에 소문자를 대문자로 바꾸는
다른 신박한 아이디어는 없었다.


### 내 풀이
```python
def Jaden_Case(s):
    # 함수를 완성하세요
    ns = ''
    for i in s.split():
        ns += i.title() + ' '
    return ns.strip()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
```

### 다른 풀이1
```python
def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title().strip()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
```
