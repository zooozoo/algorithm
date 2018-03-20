d = {"김철수":78, "이하나":97, "정진원":88}

l = []
for k, v in d.items():
    l.append((k, v))

print(sorted(l, key=lambda x: x[0]))

print(type(d.items()))