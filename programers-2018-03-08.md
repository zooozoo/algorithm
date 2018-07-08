# 문제
number_generator함수는 x와 n을 입력 받습니다.
2와 5를 입력 받으면 2부터 시작해서 2씩 증가하는 숫자를 5개 가지는 리스트를 만들어서 리턴합니다.
[2,4,6,8,10]

4와 3을 입력 받으면 4부터 시작해서 4씩 증가하는 숫자를 3개 가지는 리스트를 만들어서 리턴합니다.
[4,8,12]

이를 일반화 하면 x부터 시작해서 x씩 증가하는 숫자를 n개 가지는 리스트를 리턴하도록 함수 number_generator를 완성하면 됩니다.


풀이방법의 논리적 구성은 같지만 for 문을 돌린 후에 list comprehension으로도 할 수 있을 것 같아서
보이는 코드의 형태만 바꿔서도 문제를 풀어봤다. 
list comprehension으로 해결한 것이가장 깔끔한 해결 방법 인 것 같다.
다른 풀이법도 주로 간단하게 해결했는데 `list()`를 사용하여 해결한 방법이 
내 생각과는 조금 다른 방법으로 해결한 것 같아 기록해 둔다.

### 내 풀이
```python
def number_generator(x, n):
    return [x * (i + 1) for i in range(n)]

print(number_generator(2, 5))


def number_generator(x, n):
    # 함수를 완성하세요
    l = []
    for i in range(n):
        item = x * (i +1)
        l.append(item)
    return l

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(2,5))
```

### 다른 풀이1
```python
def number_generator(x, n):
    y=list(range(x, x*(n+1) ,x))
    return y

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(3,5))
```

### rnage()메서드
range()메서드는 자주 사용하는 메서드 였지만, 3번째 인자를 사용 하는 경우는 드물었다.
3번째 인자는 step의 크기를 결정하는 인자다. 
범위를 정하는 첫 번째와 두 번째 인자를 입력 할 때 주의해야 할 사항은 
첫번째 인자인 시작 점은 포함되고 마지막 인자인 끝은 포함되지 않는다는 것 이다.
간혹 헷갈리는 경우가 있으니 주의할 것