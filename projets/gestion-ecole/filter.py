L = list(range(20))
print(L)
im = []
def impair(e): return e%2!=0
for e in L:
    if impair(e):
        im.append(e)
print(im)
L2 = list(filter(lambda e : e%2!=0,L))
print(L2)