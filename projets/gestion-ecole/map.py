L = [1,2,3,4,5]

# def pow2(e):
#     return e**2

L1 = []
for e in L:
    L1.append(pow2(e))

print(L1)

L2 = list(map(lambda e: e**2,L))
print(L2)

#fonction anonyme (lambda)

f = lambda x,y,z : x+y+z

