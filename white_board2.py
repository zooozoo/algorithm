num = 123
place_value = len(str(num))
value = 0
for i in reversed(range(place_value)):
    if i is 0:
        value += num
        print(value)
        break
    value += num // (10 ** (i))
    num = num % (10 ** (i))
    print(value)



