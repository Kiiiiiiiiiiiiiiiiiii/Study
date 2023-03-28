n = input().split('-') 
list = [] 

for i in n:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    list.append(sum)

answer = list[0] 

for i in range(1, len(list)): 
    answer -= list[i]
print(answer)
