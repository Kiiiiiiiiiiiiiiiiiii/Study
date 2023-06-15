from itertools import combinations

array = []
tmp =[]

for _ in range(9):
    array.append(int(input()))

tmp = list(combinations(array, 7))

for i in tmp:
    if sum(i) == 100:
        for j in i:
            print(j)



        