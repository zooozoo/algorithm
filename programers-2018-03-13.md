# 문제
별이는 헬로월드텔레콤에서 고지서를 보내는 일을 하고 있습니다. 개인정보 보호를 위해 고객들의 전화번호는 맨 뒷자리 4자리를 제외한 나머지를 "*"으로 바꿔야 합니다.
전화번호를 문자열 s로 입력받는 hide_numbers함수를 완성해 별이를 도와주세요
예를들어 s가 "01033334444"면 "*******4444"를 리턴하고, "027778888"인 경우는 "*****8888"을 리턴하면 됩니다.

# 새로 알게된 것
나의 풀이가 거의 스탠다드한 형태, 다른 언어는 어떻게 해결하는지는 모르겠지만
파이썬 으로는 비교적 간단하게 해결할 수 있는 문제인 것 같다.
다른 풀이중에 기억에 남는 것은 `replace()`메서드를 사용해 문제를 해결 했던게 기억에 남는다.


### 내 풀이
```python
def hide_numbers(s):
    return (len(s[:-4])*'*') + s[-4:]
    # 함수를 완성해 별이를 도와주세요

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'))
```

### 다른 풀이1
```python
def hide_numbers(s):
    return s.replace(s[:-4],'*'*len(s[:-4]))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));
```