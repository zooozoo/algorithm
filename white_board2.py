s = "3people unFollowed me for the last week"

ns = ''

for i in s.split():
    ns += i.title() + ' '

print(ns)