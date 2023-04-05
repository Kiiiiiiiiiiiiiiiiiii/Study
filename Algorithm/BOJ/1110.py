n = int(input())
cnt = 0
t = n // 10
o = n % 10


while True:
    tmp = 0
    tmp2 = 0
    tmp = t+o
    tmp2 = int(str(o)+str(tmp % 10))
    cnt+=1
    if n == tmp2:
        break
    t = o
    o = tmp % 10

print(cnt)
