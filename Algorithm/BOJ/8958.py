n = int(input())

for _ in range(n):
    cnt = 0
    ans = 0
    ox = input()
    for i in range(len(ox)):
        if ox[i] == 'O':
            cnt +=1
            ans += cnt
        else:
            cnt = 0
    print(ans)
        