n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

ans = {}

for i in nlist:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1

for i in mlist:
    if i in ans:
        print(ans[i], end = ' ')
    else:
        print(0, end = ' ')
