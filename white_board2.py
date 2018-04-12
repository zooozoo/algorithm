def adder(a, b):
    if a < b :
        result = 0
        for i in range(a,b+1):
            result += i
        return result
    elif b < a :
        result = 0
        for i in range(b, a+1):
            result += i
        return result
    else:
        return a




print(adder(3,5))



# for i in range(3, 5):
#     print(i)