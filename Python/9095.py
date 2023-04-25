n = int(input())

def sum(m):
    if m ==1:
        return(1)
    elif m ==2:
        return(2)
    elif m ==3:
        return(4)
    elif m>3:
        return sum(m-1)+sum(m-2)+sum(m-3)

for i in range(n):
    m =int(input())
    print(sum(m))