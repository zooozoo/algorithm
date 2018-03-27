# 문제
digit_reverse함수는 양의 정수 n을 매개변수로 입력받습니다.
n을 뒤집어 숫자 하나하나를 list로 표현해주세요
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴하면 됩니다.

# 새로 알게된 것
문제를 해결하는 방법은 거의 비슷했다. for문을 두개 돌리면서 두 번째 for문에서 검사할 대상보다 작은 모든 정수를 순회하며
1과 자기 자신을 제외한 다른 정수로 대상 숫자가 나누어 지는지를 확인하는 것 이다.
차이점으로 갈리는 것은 검사한 숫자를 어떻게 표시할 것인지, 그리고 결과를 어떻게 바로 보여 줄 것인지가 달랐다.
눈에 띄었던 해결 방법으로는 `for else`문을 사용한 풀이방법이 있다. 

['for else'문 사용에 관해 포스팅한 블로그 링크](http://www.mukgee.com/?p=93)

그냥 메서드가 아니라 수학문제를 해결 하는 것처럼 논리적인 구성을 바탕으로 해결하는 문제가 나올 때 마다
여러가지 해결 방법 중에서 어떤 방법이 가장 좋은 해결 방법인지가 고민이 된다.
직관적으로는 실행시간을 체크해야 될 것 같고 그런 비교가 들어가야만 알고리즘 연습이 더 의미를 가질 수 있을 것 같다.


### 내 풀이
```python
def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    result = [i for i in range(2, n+1)]

    for i in range(n):
        item = i + 1
        for a in range(2, item):
            if item % a == 0:
                result.remove(item)
                break

    return len(result)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))
```

### 다른 풀이1
```python
def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    count=0
    for n in range(2,n+1):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            count+=1
    return count


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))
```

### 다른 풀이2
```python
def numberOfPrime(n):
    list = []
    for i in range(2,n+1):
        c = True
        for j in range(2,i-1):
            if i%j == 0:
                c = False
                break
        if c:
            list.append(i)
    return len(list)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))
```