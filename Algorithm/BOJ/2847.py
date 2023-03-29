n = int(input())
score = [0] * n
cnt = 0
answer = 0
for i in range(n):
    score[i] = int(input())

score.reverse()

for i in range (1, n):
    if score[i] >= score[i-1]:
        cnt = (score[i] - score[i-1]) + 1
        score[i] -= cnt
        answer += cnt

print(answer)
