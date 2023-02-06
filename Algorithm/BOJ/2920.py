data = list(map(int, input().split()))

asc = [1,2,3,4,5,6,7,8]
desc = [8,7,6,5,4,3,2,1]

if data == asc :
    print("ascending")
elif data == desc:
    print("descending")
else :
    print("mixed")
    
    
## 다른 방식
## 다음값과 비교해서 계속 오름차순이면 asc, 계속 내려가면 desc 아니면 mix

data = list(map(int, input().split()))

asc = True
desc = True

for i in range(1,8):
    if data[i] > data[i-1]:
        desc = False
    elif data[i] < data[i-1]:
        asc = False

if asc :
    print("ascending")
elif desc:
    print("descending")
else :
    print("mixed")
    
    
