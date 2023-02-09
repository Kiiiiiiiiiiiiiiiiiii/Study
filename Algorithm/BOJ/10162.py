time = int(input())
#300  60   10
five, one, sec =0,0,0

while time > 0:
    if time % 10 != 0 : #1의 자리에 0이 아닌 숫자가 있으면 바로 -1
        print(-1)
        break  
    else:      
        if time // 300 >= 1:
            five += time // 300
            time -= 300 * (time // 300)
        if time // 60 >= 1:
            one += time // 60
            time -= 60 * (time // 60)
        if time // 10 >= 1:
            sec += time // 10
            time -= 10 * (time // 10)
    print(five, one, sec)
