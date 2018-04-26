def nlcm(num):
    def gcd(a, b):
        while (b != 0):
            temp = a % b
            a = b
            b = temp
        return abs(a)

    # 최소공배수 구하는 함수
    def lcm(a, b):
        gcd_value = gcd(a, b)
        if gcd_value == 0:
            return 0
        return a * b // gcd(a, b)

    for i in range(len(num) - 1):
        a = num.pop(0)
        b = num.pop(0)
        num.append(lcm(a, b))

    return num[0]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2, 6, 8, 14]))
print(nlcm([12, 11, 38, 54, 47, 47, 53, 80, 42, 18]))




# def nlcm(num):
#     answer = 0
#     max_number = max(num)
#     iterate_num = 1
#     while True:
#         result = True
#         for i in num:
#             if max_number * iterate_num % i != 0:
#                 result = False
#                 break
#         else:
#             answer = max_number * iterate_num
#             break
#         iterate_num += 1
#     return answer
#
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(nlcm([2, 6, 8, 14]))

# 최소공배수 구하는 공식 http://math7.tistory.com/145



# def nlcm(num):
#     answer = 0
#     max_number = max(num)
#     num.remove(max_number)
#     iterate_num = 1
#     while True:
#         result = True
#         for i in num:
#             if max_number*iterate_num % i != 0:
#                 result = False
#         if result == True:
#             answer = max_number*iterate_num
#             break
#         print(f'iterate_num {iterate_num}')
#         iterate_num += 1
#     return answer

#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(nlcm([12, 11, 38, 54, 47, 47, 53, 80, 42, 18]))
