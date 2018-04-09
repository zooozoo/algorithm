A = [[2],[2]]
B = [[1, 2]]

# a의 행 갯수와, b의 열 갯수가 같아야 한다.
# A의 행 갯수, B의 열 갯수가 최종 만들어야할 행렬의 모습이 됨
# 결국 A의 행 갯수, B의 열 갯수만큼 순회해야만 함

# a의 행의 갯수
h = len(A)

# b의 열의 갯수는 b리스트가 가지고 있는 리스트의 갯수
y = len(B[0])

result_d = {}
# 행 순회
# for num1 in range(h):
#     # 열 순회
#     for num2 in range(y):
#
#         # print(f'B[num1][num2] {B[num1][num1]}')
#         for num3 in range(len(A[num1])):
#             # print('---------------------------------')
#             # print(f'{num1+1}행 {num3+1}열')
#             # print(f'A[{num1}][{num2}] {A[num1][num2]}')
#             # print(f'B[{num2}][{num3}] {B[num2][num3]}')
#
#             if f'{num1+1}행 {num3+1}열' in result_d:
#                 add = result_d[f'{num1+1}행 {num3+1}열'] + A[num1][num2] * B[num2][num3]
#                 result_d[f'{num1+1}행 {num3+1}열'] = add
#                 continue
#             result_d[f'{num1+1}행 {num3+1}열'] = A[num1][num2] * B[num2][num3]

for num1 in range(h):
    for num2 in range(y):
        for num3 in range(len(A[num1])):
            if f'{num1+1}행 {num2+1}열' in result_d:
                result_d[f'{num1+1}행 {num2+1}열'] += A[num1][num3] * B[num3][num2]
                # add = result_d[f'{num1+1}행 {num2+1}열'] + A[num1][num3] * B[num3][num2]
                # result_d[f'{num1+1}행 {num2+1}열'] = add
                continue
            result_d[f'{num1+1}행 {num2+1}열'] = A[num1][num3] * B[num3][num2]
            # print(f'{num1}행 {num2}열')
            # print(f'A[{num1}][{num3}] {A[num1][num3]}')
            # print(f'B[{num3}][{num2}] {B[num3][num2]}')

print(result_d)


result_l = []
for i1 in range(h):
    ml = []
    for i2 in range(y):
        item = result_d[f'{i1+1}행 {i2+1}열']
        ml.append(item)
        print(item)
    result_l.append(ml)

print(result_l)



# A = [[2],[2]]
# B = [[1, 2]]
#
# matR = [ len(B[0])*[0] for i in range (len(A)) ]
# print(matR)
#
# for i in range (len(matR) ):
#     # 완성할 행렬의 행 순회
#     print('---------')
#     print('i =', i)
#     for j in range ( len(matR[i]) ):
#         # 해당 행의 열 순회
#         for k in range ( len(A[i] ) ):
#             # A의 행 순회
#             print('j =', j)
#             print('k =', k)
#             matR[i][j] += A[i][k]*B[k][j]
#
#
# print(matR)
# print(len(B[0]))
# print(3*[0])

