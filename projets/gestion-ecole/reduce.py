from functools import reduce
L = [1,2,3,4] # 1^2 + 2^2...

S = 0 
for e in L:
    S += e**2

print(S)

S2 = reduce(lambda s,e : s+e**2,L,0)
print(S2)