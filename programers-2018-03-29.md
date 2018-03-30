# 문제
자연수로 이루어진 길이가 같은 수열 A,B가 있습니다. 최솟값 만들기는 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱한 값을 누적하여 더합니다. 이러한 과정을 수열의 길이만큼 반복하여 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다.

예를 들어 A = [1, 2] , B = [3, 4] 라면

A에서 1, B에서 4를 뽑아 곱하여 더합니다.
A에서 2, B에서 3을 뽑아 곱하여 더합니다.
수열의 길이만큼 반복하여 최솟값 10을 얻을 수 있으며, 이 10이 최솟값이 됩니다.
수열 A,B가 주어질 때, 최솟값을 반환해주는 getMinSum 함수를 완성하세요.

# 새로 알게된 것
A에서 가장 큰 수, B에서 가장 작은 수를 곱하고, 그 다음에는 A에서 두번째로 큰 수, B에서 두번재로 큰 수를 곱하는 식으로 점점
오름차순과 내림차순의 순서로 A와 B의 원소들을 곱한값을 더하면 가장 최소값이 나온다는 사실을 안다면 어느정도 쉽게 해결할 수 있는 문제다.

그런데 나는 이 문제를 A는 그대로 두고, B리스트의 모든 순서 조합들의 리스트를 구해서 각각의 경우의 수를 모두 구해서 가장 최솟값을 구하려고
시도 했다. 2시간을 넘게 생각했지만 쉽사리 해결 되지 않았다. 
그래서 모든 경우의 수를 구하기 위해선 어떻게 해야할지 검색해보니 순열을 만들면 되는데 이 순열을 만들기 위해서는 재귀함수에 대한 이해가 필요했다.
물론 꼭 재귀함수로만 순열을 만들 수 있는 것은 아니지만 어쨌든 그와 비슷한 개념을 어느정도 이해하고 있어야만 순열함수를 잘 이해할 수 있는 것 같다.

순열로 문제를 해결하려다가 잘 안되서 결국 검색으로 힌트를 얻어 해결했다.

하지만 순열에 대한 아쉬움이 남아서 보고 도움이 되는 링크와 함수를 기록에 남긴다. 
공부가 많이 되었다.


[순열 함수 출처: http://codepractice.tistory.com/59](http://codepractice.tistory.com/59)
[재귀 함수에 대한 상세한 설명](https://ko.wikibooks.org/wiki/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EA%B0%80_%EC%95%84%EB%8B%8C_%EC%9D%B4%EB%93%A4%EC%9D%84_%EC%9C%84%ED%95%9C_%ED%8C%8C%EC%9D%B4%EC%8D%AC_3_%EC%9E%90%EC%8A%B5%EC%84%9C/%EA%B3%A0%EA%B8%89_%ED%95%A8%EC%88%98_%EC%98%88%EC%A0%9C)
[순열을 생성하는 여러가지 방법](https://code.i-harness.com/ko/q/197e4)


### 내 풀이
```python
def getMinSum(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2,3],[4,5,6]))
```

### 순열을 만드는 재귀함수들
```python
def perm(a):
    length = len(a)
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in perm(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
        return result
        
def permutList(l):
    if not l:
            return [[]]
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res.extend([[e] + r for r in permutList(temp)])

    return res
        
```
