import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    list[i] = max(list[i], list[i] + list[i-1])
    
print(max(list))