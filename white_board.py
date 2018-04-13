def getDayName(a,b):
    nd2 = {1: 0, 2: 31, 3: 60, 4: 91, 5: 121, 6: 152, 7: 182, 8: 213, 9: 244, 10: 274, 11: 305, 12: 335}
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    num = (nd2[a] + b) % 7
    answer = days[num]
    return answer

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(1,1))