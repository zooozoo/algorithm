# 문제
행렬의 곱셈은, 곱하려는 두 행렬의 어떤 행과 열을 기준으로, 
좌측의 행렬은 해당되는 행, 우측의 행렬은 해당되는 열을 순서대로 곱한 값을 더한 값이 들어갑니다. 
행렬을 곱하기 위해선 좌측 행렬의 열의 개수와 우측 행렬의 행의 개수가 같아야 합니다. 
곱할 수 있는 두 행렬 A,B가 주어질 때, 행렬을 곱한 값을 출력하는 productMatrix 함수를 완성해 보세요.

# 새로 알게된 것
리스트와 `zip()`메서드를 활용하는 것에 대해서 알게 되었다.
행렬을 모양으로 만들어서 직접 연산을 해보는 것 과는 다르게 리스트로 되어있는 것을 다시 행렬의 곱셈에 알맞게 
순회하려고 하니 어려움을 겪었다. 
목표를 놓고 차분하게 한단계씩 문제를 해결해 나가면 되는데 중간에 꼬이면 답을 찾는 전체 과정이 꼬이는 일을 
반복했다. 결국 3일 간에 시간을 투자하며 들여다 본 결과로 그 흐름을 단계적으로 잘 이어나갈 수 있었다.

다른 사람들이 해결한 방법 중에는 리스트를 잘 이용해 해결한 방법과 `zip()`메서드를 잘 활용한 방법이 있었는데
`zip()`메서드를 활용한 경우에는 리스트 컴프리핸션을 사용해야만 한다.
둘다 기록해 둔다.


리스트 곱셈의 결과
```python
>>> a = [10, 20, 30]
>>> b = a * 3
>>> b
[10, 20, 30, 10, 20, 30, 10, 20, 30]
```
[참고 블로그](http://covenant.tistory.com/28)


### 내 풀이
```python
def productMatrix(A, B):
    answer = []
    h = len(A)
    y = len(B[0])

    result_d = {}

    for num1 in range(h):
        for num2 in range(y):
            for num3 in range(len(A[num1])):
                if '{}행 {}열'.format(num1+1, num2+1) in result_d:
                    result_d['{}행 {}열'.format(num1+1, num2+1)] += A[num1][num3] * B[num3][num2]
                    continue
                result_d['{}행 {}열'.format(num1+1, num2+1)] = A[num1][num3] * B[num3][num2]

    for i1 in range(h):
        ml = []
        for i2 in range(y):
            item = result_d['{}행 {}열'.format(i1+1, i2+1)]
            ml.append(item)
        answer.append(ml)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [[ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a,b)))
```

### 다른 풀이1
```python
def productMatrix(mat1, mat2):
    matR = [ len(mat2[0])*[0] for i in range (len(mat1)) ]
 
    for i in range (len(matR) ):
        for j in range ( len(matR[i]) ):
            for k in range ( len(mat1[i] ) ):
                matR[i][j] += mat1[i][k]*mat2[k][j]
 
    return matR
```

### 다른 풀이2
```python
def productMatrix(A, B):
    answer = []
    for i in range(len(A)):
        tmp = []
        for j in range(len(A[0])):
            element = 0
            for k in range(len(A[0])):
                element += A[i][k]*B[k][j]
            tmp.append(element)
        answer.append(tmp)
    return answer
```

### 다른 풀이3
```python
def productMatrix(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


a = [[1, 2], [2, 3]]
b = [[3, 4], [5, 6]]

print("결과 : {}".format(productMatrix(a, b)))
```

