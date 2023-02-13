import hashlib

n = input()
encode = n.encode()
answer = hashlib.sha256(encode).hexdigest() #파이썬에서 hashlib으로 sha256 간단하게 구현 가능
print(answer)
