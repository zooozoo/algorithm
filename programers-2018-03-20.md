# 문제

딕셔너리는 들어있는 값에 순서가 없지만, 키를 기준으로 정렬하고 싶습니다. 
그래서 키와 값을 튜플로 구성하고, 이를 순서대로 리스트에 넣으려고 합니다.
예를들어 {김철수:78, 이하나:97, 정진원:88}이 있다면 각각의 키와 값을

(김철수, 78)
(이하나, 97)
(정진원, 88)
과 같이 튜플로 분리하고 키를 기준으로 정렬해서 다음과 같은 리스트를 만들면 됩니다.
[ (김철수, 78), (이하나, 97), (정진원, 88) ]

다음 sort_dictionary 함수를 완성해 보세요.

# 새로 알게된 것
파이썬의 내장함수를 사용해야 할 것 같은 느낌이 강력하게 들어서 찾아가면서 문제를 해결했다.
다른 풀이들을 보면서 `sorted()`메서드가 반환하는 자료형과 사용법을 잘 익혔다면 정말 간단하게 
해결할 수 있는 문제라는 것을 알게 되었다.

파이썬 딕셔너리에 `.items()`메서드를 사용하면 dict_items 클래스 인스턴스가 나오는데 내용물을
튜플로 이루어진 리스트 이다. 해당 인스턴스에 `sorted()`를 사용하면 튜플로 이루어진 리스트를 반환하게 된다.
대부분의 사람들은 sorted의 두 번째 인자에 `key=lambda x: x[0]`와 같이 key값을 할당하여 순서를 비교할 값을
설정했는데 가장 간단하게 해결한 풀이에서는 key값을 생략했다.  
`sorted()`메소드가 안의 내용물들이 또다시 list나 여러 값을 가지고 있는 경우 가장 첫번째 값을 기준으로 정렬하고
만약에 값이 같으면 두 번째 값을 기준으로 정렬해 준다. 

관련내용 링크
[파이썬 공식문서](https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts)
[블로그](https://www.peterbe.com/plog/in-python-you-sort-with-a-tuple)



### 내 풀이
```python
def sort_dictionary(dic):
    '''입력받은 dic의 각 키와 값을 튜플로 만든 다음, 키 값을 기준으로 정렬해서 리스트에 넣으세요. 그 리스트를 return하면 됩니다.'''
    l = []
    for key, value in dic.items():
        l.append((key, value))
    return sorted(l, key=lambda x: x[0])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( sort_dictionary( {"김철수":78, "이하나":97, "정진원":88} ))
```


### 다른 풀이1
```python
def sort_dictionary(dic):
    return sorted(dic.items(), key=lambda x: x[0])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( sort_dictionary( {"김철수":78, "이하나":97, "정진원":88} ))
```

### 다른 풀이2
```python
def sort_dictionary(dic):
    return sorted(dic.items())

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( sort_dictionary( {"김철수":78, "이하나":97, "정진원":88} ))
```
