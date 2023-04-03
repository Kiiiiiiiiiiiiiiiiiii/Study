n = input().casefold()
list = list(set(n))
size = []

for i in list:
    cnt=n.count(i)
    size.append(cnt)

if size.count(max(size)) > 1:
    print('?')
else:
    print(list[(size.index(max(size)))].upper())
