n = int(input())
answer = 0
cnt =0
for i in range(1, n+1):
    answer += i
    cnt += 1
    if (answer > n):
        cnt-=1
        break
print(cnt)