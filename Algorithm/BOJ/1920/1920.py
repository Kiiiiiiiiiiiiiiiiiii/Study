n = int(input())
nlist = set(map(int, input().split())) #list로 받을때 타임아웃 set O(1)이어서 set으로 
m = int(input())
mlist = list(map(int, input().split()))


for i in mlist:
    if i in nlist:
        print(1)
    else:
        print(0)
        
