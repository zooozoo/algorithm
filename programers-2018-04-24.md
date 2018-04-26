# 문제
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
예를 들어 2와 7의 최소공배수는 14가 됩니다. 
정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
nlcm 함수를 통해 n개의 숫자가 입력되었을 때, 최소공배수를 반환해 주세요. 
예를들어 [2,6,8,14] 가 입력된다면 168을 반환해 주면 됩니다.

# 새로 알게된 것
처음에 while문으로 정답을 구해냈지만, 인자로 주어지는 리스트가 길어질 수록 시간이 너무 많이 걸려서 시간초과로
통과하지 못했다. 
최대공약수와 최소공배수 두가지를 구하는 방법을 잘 알고 있어야 했는데, 문제를 해결하기에 너무 많은 시간이 할애 되었기에
구글신과 접선하여 문제를 해결했다.
대부분의 사람들이 최소공배수 알고리즘을 구현하기 위해서 최대공약수를 활용하는 것을 주로 활용 했다.
내장함수를 사용하지 않으면서도 가장 간단하게 구현했다고 생각되는 해결방법을 기록해 둔다.
내가 생각하는 모범답안의 작성자가 급했는지 필요없는 주석과 코드를 남겨 놓았지만 진짜 심플하게 잘 풀어냈다.
수학적인 센스가 잇어서 그런건지 아니면 코드를 잘짜는 센스가 있어서 그런건지 그것도 아니면
그냥 원래 코드를 잘 짜던 사람인지... 부러웠다. 
언젠간 나도 저렇게 센스있는 코드를 짤 수 있었으면 좋겠다.


### 내 풀이
```python
def nlcm(num):
    def gcd(a, b):
        while (b != 0):
            temp = a % b
            a = b
            b = temp
        return abs(a)

    # 최소공배수 구하는 함수
    def lcm(a, b):
        gcd_value = gcd(a, b)
        if gcd_value == 0:
            return 0
        return a * b // gcd(a, b)

    for i in range(len(num) - 1):
        a = num.pop(0)
        b = num.pop(0)
        num.append(lcm(a, b))

    return num[0]
```

### 다른 풀이1
```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def nlcm(num):
    temp = 1
    for i in range(len(num)):
        temp = (num[i] * temp) / (gcd(num[i], temp))
    return temp
```
