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

