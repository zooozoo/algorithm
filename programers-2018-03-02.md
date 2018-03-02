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


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));
```
