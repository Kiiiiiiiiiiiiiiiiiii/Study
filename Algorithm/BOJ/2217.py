n = int(input())
list = []
answer = []

for i in range(n):
    list.append(int(input()))
list.sort()

for i in list:
    answer.append(i * n)
    n-=1


print(max(answer))
