# 문제

양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를들어 18의 자릿수 합은 1+8=9이고, 
18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.

Harshad함수는 양의 정수 n을 매개변수로 입력받습니다. 이 n이 하샤드수인지 아닌지 판단하는 함수를 완성하세요.
예를들어 n이 10, 12, 18이면 True를 리턴 11, 13이면 False를 리턴하면 됩니다.

# 새로 알게된 것
숫자열을 문자열로 바꾼후에 해당 자리수를 순회하면서 각 자릿수 값을 가져오는 것은 이전에도 했던 방법이라
금방 생각날 수 있었다. 
시간에 쫓겨서 그렇게 하긴 했지만 대부분의 답변들이 나와 같은 방법이었고 몇몇 답변은 수학적인 답변 내용이 있어서 
기록해 둔다.


### 내 풀이
```python
def Harshad(n):
    # n은 하샤드 수 인가요?
    number_to_string = str(n)
    added = 0
    for i in number_to_string:
        added += int(i)
    if n % added == 0:
        return True
    return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(11))
```

컴프리 핸션을 통해 `sum()`메서드를 잘 이용한 간단한 답변
### 다른 풀이1
```python
def Harshad(n):
    return n % sum(int(x) for x in str(n)) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
```

논리적으로 풀어낸 답변
### 다른 풀이2
```python
def Harshad(n):
    # n은 하샤드 수 인가요?
    origin_n=n
    sum_number=0
    while n>0 : 
        sum_number+=n%10
        n=n//10

    if origin_n%sum_number==0 : return True
    else : return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(13))
```
