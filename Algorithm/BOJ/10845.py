import sys
from collections import deque

dq = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    x = sys.stdin.readline().split()

    if x[0] == 'push':
        dq.append(x[1])
    elif x[0] == 'front':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[0])
    elif x[0] == 'back':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[len(dq)-1])    
    elif x[0] == 'size':
        print(len(dq))
    elif x[0] == 'empty':
        if len(dq) == 0:
            print('1')
        else:
            print('0')
    elif x[0] == 'pop':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[0])
            dq.popleft()