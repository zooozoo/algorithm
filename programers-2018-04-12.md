# 문제

adder함수는 정수 a, b를 매개변수로 입력받습니다.
두 수와 두 수 사이에 있는 모든 정수를 더해서 리턴하도록 함수를 완성하세요. a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
예를들어 a가 3, b가 5이면 12를 리턴하면 됩니다.

a, b는 음수나 0, 양수일 수 있으며 둘의 대소 관계도 정해져 있지 않습니다.

# 새로 알게된 것
다른 사람들이 풀이한 것들을 보면 생각보다 다양한 메서드가 사용된 것 같다. 
새로 알게 된 것과 몇가지 기발하다고 생각한 것들을 기록해 둔다.


* `abs()`메서드 : 절대값을 구하는 메서드


### 내 풀이
```python
def adder(a, b):
    if a < b :
        result = 0
        for i in range(a,b+1):
            result += i
        return result
    elif b < a :
        result = 0
        for i in range(b, a+1):
            result += i
        return result
    else:
        return a
```


### 다른 풀이1
```python
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
```
가장 간단하게 해결한 것 같다.


### 다른 풀이2
```python
def adder(a, b):
    # 함수를 완성하세요
    return sum(range(min(a,b), max(a,b)+1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
```
파이썬 함수를 잘 활용한 케이스


### 다른 풀이3
```python

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
```
로직은 이해가 되는데 공식이 이해가 안되서 적어놓음...
