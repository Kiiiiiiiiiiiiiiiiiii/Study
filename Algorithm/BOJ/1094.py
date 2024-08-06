n = int(input())

max = 64
ans = 0

while n:
    if max <= n:
        n -= max
        ans +=1
    max //=2

print(ans)