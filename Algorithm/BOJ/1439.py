n = str(input())

o = n.split('1')
z = n.split('0')

cnt_0 = 0
cnt_1 = 0


for i in o:
    if '0' in i:
        cnt_1 += 1
    

for j in z:
    if '1' in j:
        cnt_0 += 1

print(min(cnt_0, cnt_1))
