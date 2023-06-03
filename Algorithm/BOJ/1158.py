n, m = map(int,input().split())
q = [i for i in range(1,n+1)]

result = []
cnt = 0

for i in range(n):
    cnt += m-1
    if cnt >= len(q):
        cnt = cnt%len(q)
    result.append(str(q.pop(cnt)))
print("<", ", ".join(result), ">", sep = '')