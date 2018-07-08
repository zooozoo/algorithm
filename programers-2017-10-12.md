# 문제
삼각형출력하기
Level 1
printTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.
다음을 참고해 `*`(별)로 높이가 num인 삼각형을 문자열로 리턴하는 printTriangle 메소드를 완성하세요
printTriangle이 return하는 String은 개행문자('\n')로 끝나야 합니다.

```
높이가 3일때

*
**
***

높이가 5일때

*
**
***
****
*****
```

### 내 풀이
```python
def printTriangle(num):
    s = ''
    for i in range(num+1):
        s += '*'*i
        s += '\n'
    #함수를 완성하세요
    return s


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )
```

### 다른 풀이1
```python
def printTriangle(num):
    return ''.join(['*'*i + '\n' for i in range(1,num+1)])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )
```

### 다른 풀이2
```python
def printTriangle(num):
    s = ""
    for row in range(1, num+1):
        s += ('*' * row + '\n')
    return s

# '*' * 1 + '\n'
# '*' * 2 + '\n'
# '*' * 3 + '\n'
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )
```
