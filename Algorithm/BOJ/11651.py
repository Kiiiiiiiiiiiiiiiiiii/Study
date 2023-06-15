n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

arry={}

#a를 k v로 arry에 저장
for i in a:
    if i in arry:
        arry[i] += 1
    else:
        arry[i] = 1

# arry에 b의 값이 있으면 출력
for i in b:
    if i in arry:
        print(arry[i], end=' ')
    else:
        print(0, end=' ')