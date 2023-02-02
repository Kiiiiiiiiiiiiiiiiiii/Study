n = int(input())
cnt =0
if n % 5 == 0:
    cnt += (n//5)
    print(cnt)
else :
    while n > 1 :
        n-=2
        cnt += 1
        if n % 5 == 0:
            cnt += (n//5)
            print(cnt)
            break
    else:
        print(-1)
