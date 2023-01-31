def solution(number, k):
    list = []
    
    for i in number:
        while list and list[-1] < i and k > 0:
            k -= 1
            list.pop()
        list.append(i)
        
    if k != 0:
        list = list[:-k]

    return ''.join(list)

## 주어진 number에서  k 만큼뺐을때, 남은숫자에서 최대값
## 큰순으로 정렬하여 k만큼 잘라서 하는것이 아닌 숫자는 이어지되 그중에서 가장 큰값
