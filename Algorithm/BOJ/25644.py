import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

min, ans = list[0], 0

for i in range(1, n):
  if min < list[i]:
    ans = max(ans,list[i]-min)
  else:
    min = list[i]

print(ans)