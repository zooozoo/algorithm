# 문제

2016년 1월 1일은 금요일입니다. 2016년 A월 B일은 무슨 요일일까요? 
두 수 A,B를 입력받아 A월 B일이 무슨 요일인지 출력하는 getDayName 함수를 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각

SUN,MON,TUE,WED,THU,FRI,SAT

를 출력해주면 됩니다. 예를 들어 A=5, B=24가 입력된다면 5월 24일은 화요일이므로 TUE를 반환하면 됩니다.

# 새로 알게된 것
어찌됬건 푸는 방법은 대동소이하다.
datetime모듈로 해결한 것과 조금 더 깔끔한 코드로 문제를 해결한 케이스를 기록해 둔다.


### 내 풀이
```python
def getDayName(a,b):
    nd2 = {1: 0, 2: 31, 3: 60, 4: 91, 5: 121, 6: 152, 7: 182, 8: 213, 9: 244, 10: 274, 11: 305, 12: 335}
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    num = (nd2[a] + b) % 7
    answer = days[num]
    return answer

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(1,1))
```


### 다른 풀이1
```python
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]


#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
```


### 다른 풀이2
```python
def getDayName(a,b):
    monthDay = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    weakName = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return weakName[(sum(monthDay[0:a]) + b) % 7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
```
