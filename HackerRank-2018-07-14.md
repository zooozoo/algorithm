![problem](hackeRank-problem/hackerRank-2018-07-14.jpg)

### answer

```python
def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i, row in enumerate(arr):
        left_to_right += row[i]
    for i, row in enumerate(reversed(arr)):
        right_to_left += row[i]
    return abs(left_to_right-right_to_left)
```
3가지 정도롤 기록해 놔야 할 듯 하다.

1. enumerate의 결과물이 뭘까.
    문서의 내용을 먼저 참조해 보자 [링크](https://docs.python.org/3/library/functions.html#enumerate)
    
    > Return an enumerate object. iterable must be a sequence, an iterator, 
    or some other object which supports iteration. The `__next__()` method of 
    the iterator returned by enumerate() returns a tuple containing a count 
    (from start which defaults to 0) and the values obtained from iterating 
    over iterable.
    
    해석해 보자면
    
    > enumerate 객체를 반환한다. sequence, 또는 iterator 또는 순회가능한 객체여야 합니다. 
    enumerate()에서 return되는 iterator의 `__next__()`메서드는 0부터시작 하는 숫자로 된 순서와 
    iterable객체를 순회하며 얻은 값을 묶어 튜플 형태로 반환합니다.
    
    몇줄 안되는 구분을 해석하면서도 어려움을 느꼈다. 해석실력이 부족함은 알겠는데, 더하여 파이썬에서 
    내가 모르는 부분이 있기 때문에 정확하게 해석하기에 어려움을 느끼지 않았나 싶다.
    그중 하나를 함께 기록해놓자면 sequence.....
    
    sequence는 python자료형의 하나다. 자료형을 알긴 알아도 이걸 sequence라고 부르는지는 몰랐다..
    문자열, 리스트, 튜플과 같은 자료형을 시퀀스라고 하며, 인덱싱, 슬라이싱 등을 할 수 있다.
    관련내용이 친절하게 설명되어 있는 블로그를 발견하여 링크를 남긴다 [링크])(http://analyticsstory.com/31)
    
    본론으로 돌아와서 enumerate가 return하는 것은 정확하게는 enumerate object 인데 
    이 enumerate object는 순회가능 하며 각각의 item 들은 숫자와 객체에서 빼온 값을 묶어서 튜플 형식으로
    묶여 있다.
    
    따라서 아래와 같이 list로 묶어서 사용가능 하다.
    ```python
    my_list = ['apple', 'banana', 'grapes', 'pear']
    counter_list = list(enumerate(my_list, 1))
    print(counter_list)
    # Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
    ```
    enumerate 사용법 관련한 설명이 나와있는 [링크](http://book.pythontips.com/en/latest/enumerate.html)
    
2. enumerate()를 거꾸로 순회하기 [링크](https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python)
    ```python
    >>> a = ["foo", "bar", "baz"]
    >>> for i in reversed(a):
    ...     print i
    ... 
    baz
    bar
    foo
    To also access the original index:
    
    >>> for i, e in reversed(list(enumerate(a))):
    ...     print i, e
    ... 
    2 baz
    1 bar
    0 foo
    ``` 
    사실 문제에서 enumerate를 사용 할 때 숫자만 역순으로 나오는 방법을 찾았는데 그런 방법은 좀더 복잡한
    로직으로 사용해야 할 것 같다.
    
3. 절대값 구하기 [링크](https://stackoverflow.com/questions/3854310/how-to-convert-a-negative-number-to-positive)
    아래와 같이 절대값을 구할 수 있다.
    ```python
    >>> n = -42
    >>> -n       # if you know n is negative
    42
    >>> abs(n)   # for any n
    42
    ```
    