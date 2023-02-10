n = int(input())
#커서를 가운데로 생각하고 좌스택, 우스택 으로 나눠서 생각
for i in range(n):
    lstack = []
    rstack = []
    data = input()
    for j in data:
        if j == '-':
            if lstack:
                lstack.pop()
        elif j == '<':
            if lstack:
                rstack.append(lstack.pop())
        elif j == '>':
            if rstack:
                lstack.append(rstack.pop())
        else:
            lstack.append(j)
    lstack.extend(reversed(rstack)) # rstack을 reverse
print(''.join(lstack))

