# 문제
alpha_string46함수는 문자열 s를 매개변수로 입력받습니다.
s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요.
예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다

python에서 '혹시 있을까?' 하는 생각은 '역시 있군'이라고 바뀌는 경우가 많다.
이번경우가 그런 경우다. `str.isdigit()`을 사용해 문자열에 숫자로 구성되어 있는지
간단하게 확인할 수 있다. 덧붙여 `str.isalph`를 사용하면 해당 문자열이 
알파벳으로만 구성되어 있는지도 확인할 수 있다. 
다른사람의 풀이에서`len(s) in [4, 6]`은 편리하게 사용할 수 있는 부분인 것 같다.

### 내 풀이
```python
def alpha_string46(s):
    if (len(s) == 4) or (len(s) == 6):
        try:
            int(s)
            return True
        except:
            return False
    return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("4u012") )
```

### 다른 풀이1
```python
def alpha_string46(s):
    return s.isdigit() and len(s) in [4, 6]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )
```

