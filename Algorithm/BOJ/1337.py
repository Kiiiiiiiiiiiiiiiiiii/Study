n = int(input())
arr = []
ans = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

for i in range(n):
    cnt = 0
    for j in range(arr[i], arr[i]+5):
        if j  not in arr:
            cnt+=1
    ans.append(cnt)
print(min(ans))        

