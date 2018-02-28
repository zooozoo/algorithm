# 문제
제일 작은 수 제거하기
rm_small함수는 list타입 변수 mylist을 매개변수로 입력받습니다.
mylist 에서 가장 작은 수를 제거한 리스트를 리턴하고, mylist의 원소가 1개 이하인 경우는 []를 리턴하는 함수를 완성하세요.
예를들어 mylist가 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10, 8, 22]면 [10, 22]를 리턴 합니다.

### 내 풀이

```
def rm_small(mylist):
    smallest = mylist[0]
    index_num = 0
    for n in range(len(mylist)):
        if mylist[n] <= smallest:
            smallest = mylist[n]
            index_num = n
        else:
            continue
    del mylist[index_num]
    return mylist

my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))
```

### 다른 풀이1
```
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4,3,2,1]
print("결과 {} ".format(rm_small(my_list)))
```

### 다른 풀이2
```
def rm_small(mylist):
    # 함수를 완성하세요
    mylist.remove(min(mylist))
    return mylist

# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4,3,2,1]
print("결과 {} ".format(rm_small(my_list)))
```
