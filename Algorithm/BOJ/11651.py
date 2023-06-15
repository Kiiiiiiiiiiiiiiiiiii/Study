# 0 4
# 1 2
# 1 -1
# 2 2
# 3 3
# y x 를 반대로 넣어 정렬하고 다시 체크
import sys
n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    lst.append([y, x])

lst.sort()

for y, x in lst:
    print(x, y)