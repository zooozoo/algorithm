# 문제
no_continuous함수는 스트링 s를 매개변수로 입력받습니다.

s의 글자들의 순서를 유지하면서, 글자들 중 연속적으로 나타나는 아이템은 제거된 배열(파이썬은 list)을 리턴하도록 함수를 완성하세요.
예를들어 다음과 같이 동작하면 됩니다.

* s가 '133303'이라면 ['1', '3', '0', '3']를 리턴
* s가 '47330'이라면 [4, 7, 3, 0]을 리턴

### 내 풀이

```python
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
```

### 다른 풀이1
```python
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
```

새로운 리스트객체를 얻는 방법 3가지
1. copy() 함수
2. list() 변환함수
3. 슬라이스 `[:]`