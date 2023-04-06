n = input()
words =['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in words:
    n = n.replace(i,'@')
    
print(len(n))
