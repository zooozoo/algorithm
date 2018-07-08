# 문제
strToInt 메소드는 String형 str을 매개변수로 받습니다.
str을 숫자로 변환한 결과를 반환하도록 strToInt를 완성하세요.
예를들어 str이 1234이면 1234를 반환하고, -1234이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

### 내 풀이

```python
def strToInt(str):
    result = int(str)
    #함수를 완성하세요

    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));
```

### 다른 풀이1
```python
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        # str을 거꾸로 순회하기 때문에 if문은 가장 앞쪽의 부호 부분이 되며 
        # 음수일 경우 -1을 곱해서 음수로 만들어
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));
```

### 다른 풀이2
```python
def strToInt(str):
    result = 0
    #함수를 완성하세요

    if(ord(str[0]) > 48):
        num=-1
        for i in str:
            result += (ord(str[num])-48)* pow(10,abs(num+1))
            num-=1
    else:
        result= -strToInt(str[1:])
    return result

줌
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));
```

### enumerate()메서드
점프투 파이썬에 나온 설명 [링크](https://wikidocs.net/32#enumerate)

enumerate는 "열거하다"라는 뜻이다. 
이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 
인덱스 값을 포함하는 enumerate 객체를 리턴한다.

※ 보통 enumerate 함수는 아래 예제처럼 for문과 함께 자주 사용된다.

```python
>>> for i, name in enumerate(['body', 'foo', 'bar']):
...     print(i, name)
...
0 body
1 foo
2 bar
```
순서값과 함께 body, foo, bar가 순서대로 출력되었다. 
즉, 위 예제와 같이 enumerate를 for문과 함께 사용하면 
자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.

for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할때 
enumerate 함수를 사용하면 매우 유용하다.

### pow()메서드
점프투 파이썬에 나온 설명 [링크](https://wikidocs.net/32#pow)

pow(x, y)는 x의 y 제곱한 결과값을 리턴하는 함수이다.
```python
>>> pow(2, 4)
16
>>> pow(3, 3)
27
```
