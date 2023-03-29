n, m = map(int, input().split())
card = list(map(int, input().split()))

for i in range(m):
    card.sort()
    tmp=card[0]+card[1]
    card[0]=tmp
    card[1]=tmp

print(sum(card))

