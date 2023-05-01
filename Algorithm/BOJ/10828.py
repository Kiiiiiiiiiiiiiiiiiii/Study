import sys
n = int(input())
arry = []

for _ in range(n):
    msg = sys.stdin.readline().split()
    if msg[0] == 'push':
        arry.append(int(msg[1]))
    elif msg[0] == 'pop':
        if len(arry) > 0:
            print(arry.pop())
        else:
            print(-1)
    elif msg[0] == 'size':
        print(len(arry))
    elif msg[0] == 'empty':
        if len(arry) > 0:
            print(0)
        else:
            print(1)
    elif msg[0] == 'top':
        if len(arry) > 0:
            print(arry[-1])
        else:
            print(-1)