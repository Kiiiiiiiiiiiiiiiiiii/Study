n = int(input())
list = list(map(int, input().split()))
answer = 0

list.sort()
reverse = list


for i in reverse:
    if i == reverse[-1]:
        answer += i
        break
    else:
        answer += (i/2)


print(answer)
