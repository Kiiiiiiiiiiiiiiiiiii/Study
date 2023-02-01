sugar = int(input())
answer = 0
#21 : 5 5 5 3 3 
#14 : 5 3 3 3
if sugar % 5 == 0:
    print(sugar//5)
else:
    while sugar > 2:
        sugar -= 3
        answer += 1
        if sugar % 5 == 0:  
            answer += sugar // 5
            print(answer)
            break
    else:
        print(-1)
