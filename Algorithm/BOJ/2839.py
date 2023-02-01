sugar = int(input())
answer = 0

while sugar >= 0 : #설탕이 남아있는지 체크, 0아래로 내려가면 똑 떨어지게 처리 할 수 없으면 else 구문으로
    if sugar % 5 == 0 :  #설탕이 5의 배수인지 확인후 조건문 종료
        answer += sugar 
        print(answer)
        break
    sugar -= 3  #만약 5의 배수가 아니면 3키로씩 빼면서 카운트 상승, 설탕에서 3키로 뺐을때, 0미만이면 떨어지게 담을수 없으므로 -1 
    answer += 1  
else :
    print(-1)
