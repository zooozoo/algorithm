def findKim(seoul):
    kimIdx = 0
    for i in seoul:
        if i == 'Kim':
            kimIdx = seoul.index(i)
    return "김서방은 {}에 있다".format(kimIdx)


# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))