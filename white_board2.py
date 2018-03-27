result = [i for i in range(2, 11)]

for i in range(10):
    item = i +1
    print(f'{i+1} is item ')
    for a in range(2, item):
        if item % a == 0:
            print(f'item={item}, a={a}')
            result.remove(item)
            break

print(result)

# for i in range(10):
#     item = i + 1
#     for a in range(10):
#         if (a + 1) == 1 or (a + 1) == item:
#             print('1또는 자기 자신')
#         if item % (a + 1) == 0:
#             print(a + 1)
#             pass
#         result.append(item)



