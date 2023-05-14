n = input()

atoz = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numatoz=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

for i in range(len(n)):
    if n[i] in atoz:
        numatoz[atoz.index(n[i])] = i

print(*numatoz)