n = int(input())

for _ in range(n):    
    x = input()
    stack = []
    check = True
    for i in range(len(x)):
        if x[i] == '(':
            stack.append(x[i])
        if x[i] == ')':
            if stack:
                stack.pop()
            elif not stack:
                check = False
                break
    if stack or check is False:
        print('NO')
    else:
        print('YES')
