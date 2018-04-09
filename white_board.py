def productMatrix(A, B):
    answer = []
    h = len(A)
    y = len(B[0])

    result_d = {}

    for num1 in range(h):
        for num2 in range(y):
            for num3 in range(len(A[num1])):
                if '{}행 {}열'.format(num1+1, num2+1) in result_d:
                    result_d['{}행 {}열'.format(num1+1, num2+1)] += A[num1][num3] * B[num3][num2]
                    continue
                result_d['{}행 {}열'.format(num1+1, num2+1)] = A[num1][num3] * B[num3][num2]

    for i1 in range(h):
        ml = []
        for i2 in range(y):
            item = result_d['{}행 {}열'.format(i1+1, i2+1)]
            ml.append(item)
        answer.append(ml)

    return answer




# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [[ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a,b)))