n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))
ans = {}

for i in lst1:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1

for i in lst2:
    if i in ans:
        print(ans[i], end=' ')
    else:
        print(0, end = ' ')
