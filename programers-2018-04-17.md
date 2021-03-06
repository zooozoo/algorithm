# 문제
야근 지수
회사원인 수민이는 많은 일이 쌓여 있습니다. 수민이는 야근을 최소화하기 위해 남은 일의 작업량을 숫자로 메기고, 
일에 대한 야근 지수를 줄이기로 결정했습니다. 야근 지수는 남은 일의 작업량을 제곱하여 더한 값을 의미합니다. 
수민이는 1시간 동안 남은 일 중 하나를 골라 작업량 1만큼 처리할 수 있습니다. 
수민이의 퇴근까지 남은 N 시간과 각 일에 대한 작업량이 있을 때, noOvertime 함수를 제작하여 수민이의 야근 지수를 
최소화 한 결과를 출력해 주세요. 
예를 들어, N=4 일 때, 남은 일의 작업량이 [4, 3, 3] 이라면 야근 지수를 최소화하기 위해 일을 한 결과는 
[2, 2, 2]가 되고 야근 지수는 22 + 22 + 22 = 12가 되어 12를 반환해 줍니다.

# 새로 알게된 것
내가 놓쳤던 조건(야근지수가 0일 조건)을 충족시킴과 동시에 가장 간단한 방법으로 풀어낸 풀이를 기록해둔다.

알면서도 잘 써먹지 못했던 것....
리스트값 수정할 때 [https://wikidocs.net/14](https://wikidocs.net/14)
```
>>> a = [1, 2, 3]
>>> a[1] = 4
>>> a
[1, 2, 4]
```

### 내 풀이
```python
def noOvertime(n, works):
    while n > 0:
        highest = max(works)
        new = works.pop(works.index(highest)) - 1
        n -= 1
        works.append(new)
    result = 0
    for i in works:
        result += i ** 2
    return result
```

enumerate의 예
### 다른 풀이1
```python
def noOvertime(n, works):
    if n >= sum(works):
        return 0
    while n > 0:
        works[works.index(max(works))] -= 1
        n -= 1
    result = sum([w ** 2 for w in works])
    # 야근 지수를 최소화 하였을 때의 야근 지수는 몇일까요?
    return result
```
