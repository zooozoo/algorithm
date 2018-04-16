def noOvertime(n, works):
    while n > 0:
        highest = max(works)
        new = works.pop(works.index(highest)) - 1
        n -= 1
        works.append(new)
    result = 0
    for i in works:
        result += i ** 2
    return result

# 퇴근까지 남은 시간 : 26, 남은 일의 작업량 : [15, 12, 11, 15, 8, 8, 15, 12, 8, 8]
# 야근 지수를 최소화 하기 위해 일한 결과 : [9, 9, 9, 9, 8, 8, 9, 9, 8, 8]

# 퇴근까지 남은 시간 : 8, 남은 일의 작업량 : [9, 6, 11, 15, 5, 6]
# 야근 지수를 최소화 하기 위해 일한 결과 : [9, 6, 9, 9, 5, 6]



print(noOvertime(8, [9, 6, 11, 15, 5, 6]))