# 문제
nextSqaure함수는 정수 n을 매개변수로 입력받습니다.
n이 임의의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 임의의 정수 x의 제곱이 아니라면 'no'을 리턴하는 함수를 완성하세요.
예를들어 n이 121이라면 이는 정수 11의 제곱이므로 (11+1)의 제곱인 144를 리턴하고, 3이라면 'no'을 리턴하면 됩니다.

논리적으로 그렇게 어렵지 않은 문제 였던 것 같다. 
다른 사람들의 풀이에서는 `n ** 0.5`가 숫자 `n`에다 루트를 씌우는 표현이라는 것을 이용하여
내 풀이보다 더 간단하게 해결한 것들도 있었다.
and, or 연산자를 활용 한 것과 `sqrt()`메서드와 같은 것들을 알게 되었다.

# 새로 알게된 것
* `n ** 0.5`가 숫자 n에 루트를 씌운 표현식이 된다는 것과 
같은 표현을 `n ** .5`와 같은 방식으로 표현할 수 있다는 것 이다.
* return 을 and와 or 연산자를 통해 조건을 걸어 사용할 수 있다는 것을 알게 되었는데 관련 내용이 잘 이해가
가지 않아서 구글링 해 보았는데, 한글 자료에서는 제대로 설명하는 곳을 못찾았고 영어 자료에서 명쾌한 설명을 찾아 냈다.
[http://thomas-cokelaer.info/tutorials/python/boolean.html#evaluation-of-logical-and-comparison-operators-and-membership-operators](http://thomas-cokelaer.info/tutorials/python/boolean.html#evaluation-of-logical-and-comparison-operators-and-membership-operators)
* 제곱근을 반환하는 math 모듈의 `sqrt()`메서드를 사용하면 간단하게 제곱근을 구할 수 있다는 것을 알게 되었다. 

### 내 풀이
```python
def nextSqure(n):
    result = 'no'
    for i in range(n):
        if n // (i + 1) == (i + 1) and n % (i + 1) == 0:
            result = ((i + 1) + 1) ** 2
    return result
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(4)))
```

### 다른 풀이1
```python
def nextSqure(n):
    if int(n ** 0.5) ** 2 == n:
        return (int(n ** 0.5) + 1) ** 2
    else:
        return "no"

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(120)))
```

### 다른 풀이2
```python
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)))
```

### 다른 풀이3
```python
def nextSqure(n):
    from math import sqrt
    return "no" if sqrt(n) % 1 else (sqrt(n)+1)**2
```

c언어를 배우면서 되도록 실수연산은 피하는게 좋다는 이야기를 들었는데 
혹시라도 실수 연산을 해야 할 일이 있다면 참고할 만한 내용이
파이썬 코딩도장 이라는 곳의 부록에 나와있어서 링크를 남겨둔다
[링크](https://dojang.io/mod/page/view.php?id=1164)