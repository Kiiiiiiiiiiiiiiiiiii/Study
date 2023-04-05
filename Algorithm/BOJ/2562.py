list = []
for _ in range(1, 10):
    n = int(input())
    list.append(n)

print(max(list))
print(list.index(max(list))+1)
