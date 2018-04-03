# 문제
앞뒤를 뒤집어도 똑같은 문자열을 palindrome이라고 합니다.
longest_palindrom함수는 문자열 s를 매개변수로 입력받습니다.
s의 부분문자열중 가장 긴 palindrom의 길이를 리턴하는 함수를 완성하세요.
예를들어 s가 토마토맛토마토이면 7을 리턴하고 토마토맛있어이면 3을 리턴합니다.

# 새로 알게된 것
풀이방법은 크게 2부류다. 나와 비슷한 방법과, `max()`메서드를 사용한 방법
사실 `max()`를 재귀적으로 사용해서 문제를 해결할거라는 생각은 못했다. 
`max()`를 잘 사용하지 않기도 하고, 재귀도 마찬가지다. 확실히 잘 알고 있고
익숙한 사용방법을 문제해결에 동원하는 것 같다. 
물론 실행속도 관련해서는 또다른 이야기가 될 것이지만 생각하지 못했 해결 방법을 기록해 둔다.


### 내 풀이
```python
def longest_palindrom(s):
    # 함수를 완성하세요
    length = 0

    for i in range(3, len(s) + 1):
        for a in range(len(s) - i + 1):
            part = s[a:a + i]
            rev_part = part[::-1]
            if part == rev_part and length < len(part):
                length = len(part)
    return length


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("맛토마토있어"))
```

### 다른 풀이1
```python
def longest_palindrom(s):
    # 함수를 완성하세요
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))
```