# 문제
findKim 함수(메소드)는 String형 배열 seoul을 매개변수로 받습니다.

seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하세요.
seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# 새로 알게된 것
`index()`메서드를 알게 되었다. 언젠가 한번 써본 기억이 나서 금방 찾아서 해결했다.
그런데 나의 풀이는 한번에 해결할 수 있는 것을 돌아간 느낌이다.
다른 풀이에서는 `index()`메서드를 통해 간단하게 해결했다.
한편으로는 파이썬 내장함수의 위력을 느낄 수도 있었다.


### 내 풀이
```python
def findKim(seoul):
    kimIdx = 0
    for i in seoul:
        if i == 'Kim':
            kimIdx = seoul.index(i)
    return "김서방은 {}에 있다".format(kimIdx)
```

### 다른 풀이1
```python
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))
```
