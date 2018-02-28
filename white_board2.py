s = '111333444888822222233333'
l = list(s)
nl = []

if l:
    first = l.pop(0)
    nl.append(first)
    for n in range(len(l)):
        item = l.pop(0)
        if item == nl[-1]:
            pass
        else:
            nl.append(item)
        print(item)
        print('원래 list' + str(l))
        print('새로운 list' + str(nl))
        print(str(n) + '번째 루프')
else:
    print(nl)