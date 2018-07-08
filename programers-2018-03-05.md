# 문제
피보나치 수는 F(0) = 0, F(1) = 1일 때, 2 이상의 n에 대하여 
F(n) = F(n-1) + F(n-2) 가 적용되는 점화식입니다. 
2 이상의 n이 입력되었을 때, fibonacci 함수를 제작하여 n번째 피보나치 수를 반환해 주세요. 
예를 들어 n = 3이라면 2를 반환해주면 됩니다.

### 내 풀이

```python
def fibonacci(num):
    if num >= 2:
        cicle = 0
        first = 0
        second = 1
        while True:
            answer = first + second
            first = second
            second = answer
            cicle += 1
            if cicle == (num - 1):
                return answer
    elif num == 0:
        answer = num
        return answer
    elif num == 1:
        answer = num
        return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(5))
```

### 다른 풀이1

```python
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))
```

num으로 0과 1이 들어왔을 때 어떻게 처리해야 할지 고민이었는데 for문을 통해서
쉽게 해결 할 수 있었다. (사실 오류가 날꺼라고 생각했다.) **for문에 순회 범위를
0으로 잡아도 작동한다는 점은 기억할만 하다.**

내 방식으로 문제를 해결 하면서는 return과 break의 사용법상의 차이점에 대하여 
정확하게 알지 못한다는 것을 알게 되었고 추후 관련 내용에 대한 포스팅을 하면서 
정리할 것 이다.

파이썬으로 n번째의 피보나치 수열 구해내는 재귀함수
(0항이 아닌 1항부터 구함)
```python
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
```