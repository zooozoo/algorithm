# 문제
strange_sort함수는 strings와 n이라는 매개변수를 받아들입니다.
strings는 문자열로 구성된 리스트인데, 각 문자열을 인덱스 n인 글자를 기준으로 정렬하면 됩니다.
예를들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1인 문자 u, e ,a를 기준으로 정렬해야 하므로 
결과는 [car, bed, sun]이 됩니다.

strange_sort함수를 완성해 보세요.


막연한 예측으로 sorted와 lambda를 검색해 가며 방법을 찾아 해결했고, 
python으로 가장 간단하게 해결할 수 있는 해결책 인것 같다.
내 풀이 방법이 다른 많은 풀이들과 가장 유사한 방법이었고
다른 방법으로 해결한 몇가지 흥미운로운 풀이들을 기록해 놓는다.
### 내 풀이
```python
def strange_sort(strings, n):
    return sorted(strings, key=lambda a: a[n])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )
```

개인적으로는 논리적인 방법으로 해결한 것으로는 가장 좋은 풀이가 아닌가 싶다.
### 다른 풀이1
```python
def strange_sort(strings, n):
    lst = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        for j in strings:
            if j[n] == i: 
                lst.append(j)
    return lst


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )
```

