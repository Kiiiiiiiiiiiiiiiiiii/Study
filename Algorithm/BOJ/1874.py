n = int(input())

cnt=1
stack=[]
answer=[]

for i in range(1, n+1): #주어진  n 만큼 반복
    data = int(input()) 
    while cnt <= data: #현재 cnt가 입력한 data보다 적다면
        stack.append(cnt) #stack에 추가하고 증가
        cnt+=1
        answer.append('+') 
    if stack[-1] == data: #stack의 가장뒤에 값과 data가 일치하면 pop
        stack.pop() 
        answer.append('-')
    else: #오름차순으로 되지 않으면 NO
        print('NO')
        exit(0)
        
print('\n'.join(answer))
