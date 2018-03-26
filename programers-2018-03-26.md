# 문제
digit_reverse함수는 양의 정수 n을 매개변수로 입력받습니다.
n을 뒤집어 숫자 하나하나를 list로 표현해주세요
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴하면 됩니다.

# 새로 알게된 것
새로 알게 된 것은 파이썬 내장함수의 편리함, 그리고 map() 메서드의 활용이다.
주로 나와 같은 방법으로 해결하거나, `map()`메서드를 사용하거나, 아니면 슬라이스를 활용해서
문제를 해결 했다. 
`map()`메서드를 잘 활용한다면 아주 편리할거라는 생각했지만
슬라이스를 활용한 것이 가장 간단하고 깔끔한 해결책이라고 생각했다. 
(코드 가독성 면에서 말이다.)
`map()`메서드를 활용한 경우와, 슬라이스를 활용한 경우 2가지를 기록에 남긴다.

[map()메서드에 대한 한글성명](http://bluese05.tistory.com/58)
[map()메서드에 대한 파이썬 공식문서](https://docs.python.org/3/library/functions.html#map)

### 내 풀이
```python
def digit_reverse(n):
    # 함수를 완성해 주세요
    list_n = list(str(n))
    return [int(list_n.pop()) for i in range(len(list_n))]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)));
```

### 다른 풀이1
```python
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
```

### 다른 풀이2
```python
def digit_reverse(n):
    # 함수를 완성해 주세요
    answer=[]

    for i in str(n):
        answer.append(int(i))

    return answer[::-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)));
```