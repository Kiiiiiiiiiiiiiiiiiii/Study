n = int(input())
list =[]

for _ in range(n):
    x, y = list(map(int, input().split()))
    list.append([y, x])

list.sort()

for y, x in list:
    print(x, y)