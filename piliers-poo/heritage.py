class A:
    x = 1
    y = 2

class B:
    x = 3
    b = 4

class C:
    x = 5
    d = 6

class D(B,C,A):
    pass

ob = D()
print(ob.z) #MRO : method resolution order : class, mère(A,B,C)->mère->... ->object -> object has no attribute

