# 문제
1937년 Collatz란 사람에 의해 제기된 이 추측은, 입력된 수가 짝수라면 2로 나누고, 
홀수라면 3을 곱하고 1을 더한 다음, 결과로 나온 수에 같은 작업을 1이 될 때까지 반복할 경우 
모든 수가 1이 된다는 추측입니다. 
예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다. 
collatz 함수를 만들어 입력된 수가 몇 번 만에 1이 되는지 반환해 주세요. 
단, 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

# 새로 알게된 것
논리적인 면에선 for문이나 while문이나 차이가 없는 것 같다.
새로 알게되었다고 궂이이야기 하자면 while문에 else를 같이 사용한 것 정도?
지난번에 for문에 else를 사용했던 것을 기억하고 있었고, 혹시나 해서 확인해보니 while문도 같은 방식으로
사용할 수 있었다. 이번의 경우도 활용하면 유용한 기능이다. 
다른 풀이에서는 if 문을 한줄로 만들고 return하는 분기를 나눔으로써 while문의 else 같은 역할을 하게 만든점이 눈에 띄어서
기록해 둔다. 


### 내 풀이
```python
def collatz(num):
    test_number = num
    answer = 0

    while answer < 500:
        if test_number == 1:
            break
        answer += 1
        if test_number % 2 == 0:
            test_number = test_number / 2
        else:
            test_number = (test_number * 3) + 1
    else:
        answer = -1

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))
```

### 다른 풀이1
```python
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))
```
