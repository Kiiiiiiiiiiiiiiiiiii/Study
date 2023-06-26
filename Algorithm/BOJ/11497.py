n = int(input())

for i in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    max = 0 
    for j in range(2,len(arr)):
        if arr[j]-arr[j-2] > max:
            max = arr[j] - arr[j-2]

    print(max)