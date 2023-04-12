n, k = list(map(int, input().split()))
list =[]
answer = []
idx = 0
for i in range(n):
 list.append(i+1)

while list:
    idx += k-1

    if idx >= len(list):
       idx %= len(list)
    
    answer.append(str(list.pop(idx)))

print("<", ", ".join(answer), ">", sep="")
