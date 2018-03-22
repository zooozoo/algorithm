# 문제

함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
어떠한 크기의 array가 와도 평균값을 구할 수 있어야 합니다.

# 새로 알게된 것
나름 파이썬 메서드를 사용해서 간단하게 풀었다고 생각했었는데, 조금 돌아서 문제를 해결했던
거였다. `sum()`메서드의 활용을 잘 몰랐다. 덕분에 구글에 뒤져보니 한글로 iterable 한 객체에
사용할 수 있는 여러 메서드를 설명한 사이트가 있어서 기록해 둔다.

[코딩도장](https://dojang.io/mod/page/view.php?id=981)


### 내 풀이
```python
def average(array):
    # 함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
    return sum(i for i in array)/len(array)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));
```


### 다른 풀이1
```python
def average(list):
    return (sum(list) / len(list))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));
```
