n, k = list(map(int, input().split()))
val = [0]*n
cnt = 0
less = k
for i in range(n):
  val[i] = int(input())

reval = val[::-1]


for j in reval:
    if less // j != 0:
        cnt += (less//j)
        less -= (less//j) * j

print(cnt)
