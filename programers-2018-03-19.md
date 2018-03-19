# 문제
numPY함수는 대문자와 소문자가 섞여있는 문자열 s를 매개변수로 입력받습니다.
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 리턴하도록 함수를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
예를들어 s가 pPoooyY면 True를 리턴하고 Pyy라면 False를 리턴합니다.


# 새로 알게된 것
처음 작성한 코드는 조금 돌아갔지만, 다시생각해서 작성한 코드는 그래도 괜찮게 파이썬 내장함수를 잘 활용해서 만든 것 같다.
다만 조건문 `==` 비교를 통해서 바로 True, False값을 바로 리턴 할 수 있다는 것을 잊고 있었다. 

### 내 풀이
```python
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
```

### 내 풀이2
```python
def numPY(s):
    # 함수를 완성하세요
    if s.lower().count('p') == s.lower().count('y'):
        return True
    return False



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )
```

### 다른 풀이1
```python
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )
```
