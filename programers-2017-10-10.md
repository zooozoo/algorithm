### 문제
evenOrOdd 메소드는 int형 num을 매개변수로 받습니다.
num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하도록 evenOrOdd에 코드를 작성해 보세요.
num은 0이상의 정수이며, num이 음수인 경우는 없습니다.


### 내 풀이
```
def evenOrOdd(num):
    if num % 2 == 0:
        s = 'Even'
    else:
        s ='Odd'
    #함수를 완성하세요

    return s

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
```

### 다른 풀이
```
def evenOrOdd(num):
    return num % 2 and "Odd" or "Even"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
```

### 다른 풀이 해설 및 기록 / python 3항 연산자
위와 같은 방법을 3항연산이라고 한다. 파이썬에서는 3항 연산자를 다루는 방법이 2가지 있다.
첫 번째 방법은 if와 else를 이용하는 것, 두 번째 방법은 and와 or를 이용하는 것이다.


1. and, or 3항연산자의 기본 사용법은 다음과 같다.
```
condition and A or B
```
condition이 True면 A 연산이 return 되고, condition이 False면 B 가 return 된다.

2. if else를 이용한 3항연산자의 기본 사용법은 다음과 같다.
```
A if condition else B
```
condition이  True면 A 연산이 return 되고, condition이 False면 B 가 return된다.
