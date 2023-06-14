n = int(input())

code = []

for i in range(n):
    x, y = list(map(int, input().split()))
    code.append([y,x])

s_code = sorted(code)

for y,x in s_code:
    print(x, y)