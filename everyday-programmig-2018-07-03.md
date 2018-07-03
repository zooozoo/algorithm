# 문제
피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다. 
정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.
Fibonacci sequence starts with 0 and 1 where each fibonacci number is a sum of two previous fibonacci numbers. 
Given an integer N, find the sum of all even fibonacci numbers.

# 새로 알게된 것

매일 프로그래밍 이라는 곳에서 받아서 푼 문제인데 문제 답을 제공받으려면 유료 결제를 해야 한다는 사실을 알게 되었다.
실제로 작성한 코드를 돌려보는 서비스도 없는 것 같은데 유료서비스를 결제해야 할 필요성은 느끼지 못했다.
그래서 구독 해제하고 다음부터는 `heaker rank`나 `beakjoon`에서 문제를 가져와 풀기로 했다. 

### 내 풀이
```python
def even_fibo(number):
    fibo_l = []
    result_l = []
    latest_fibo_num = 0
    roop = 1
    while latest_fibo_num < number:
        if roop == 1:
            fibo_l.append(0)
            roop += 1
            continue
        if roop == 2:
            fibo_l.append(1)
            latest_fibo_num = 1
            roop += 1
            continue
        latest_fibo_num = fibo_l[-1] + fibo_l[-2]
        fibo_l.append(latest_fibo_num)
        if latest_fibo_num % 2 == 0:
            result_l.append(latest_fibo_num)
        roop += 1
    print(fibo_l)
    print(result_l)

even_fibo(2)
```

