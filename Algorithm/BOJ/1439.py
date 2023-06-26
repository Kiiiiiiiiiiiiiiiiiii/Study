n = str(input())

one = n.split('1')
zero = n.split('0')

cnt1 = 0
cnt0 = 0

for i in one:
    if '0' in i:
        cnt1 += 1

for i in zero:
    if '1' in i:
        cnt0 += 1

print(min(cnt0, cnt1))
