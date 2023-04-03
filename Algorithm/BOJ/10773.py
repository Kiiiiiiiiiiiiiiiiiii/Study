n = int(input())
list = []

for i in range(n):
    x = int(input())
    if x == 0:
        list.pop()
    else:
        list.append(x)

if (list == 0):
    print(0)
else:
    print(sum(list))
