n, m = map(int, input().split())
data = list(map(int, input().split()))
answer = 0

#주어진 숫자중에 3개를 뽑아서 m에 가장 가까운 수
for i in range(len(data)):
    for j in range(i+1,len(data)):
        for k in range(j+1, len(data)):
            sum = data[i] + data[j] + data[k] #i,j,k 를 하나씩 다 더해서 m과 비교
            if sum <= m:
                answer = max(answer, sum) # 두개의 수중 가장 큰걸 리턴

print(answer)
