def getMinSum(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    print(A)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2,3],[4,5,6]))