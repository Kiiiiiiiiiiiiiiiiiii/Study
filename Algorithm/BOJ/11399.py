n = int(input())
data = list(map(int, input().split()))
data.sort() #제일 최소로 하기 위해서 오름차순 정렬
answer = 0
time = 0

for i in data:
    answer += i
    time += answer #time 변수에 앞사람의 이용한 시간까지 값을 더해서 총 시간을 계산

print(time)
