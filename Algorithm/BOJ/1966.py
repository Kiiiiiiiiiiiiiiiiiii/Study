data = int(input())

for i in range(data):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)] #enumerate : 특정 리스트를 인덱스와 튜플형태로 만들어준다.

    cnt = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]: #큐의 가장앞쪽의 중요도가 큐의 가장큰중요도와 일치한다면 
            cnt+=1
            if queue[0][1] == m:
                print(cnt)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
