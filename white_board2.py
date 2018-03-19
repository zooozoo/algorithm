s = 'pPoooyY'
p = []
y = []
for i in s:
    if i.lower() == 'p':
        p.append(i)
    if i.lower() == 'y':
        y.append(i)

print(s.lower().count('p'))
print(s.lower().count('y'))