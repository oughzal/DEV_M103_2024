def test(n):
    if isinstance(n, int):
        return n + 1
    elif isinstance(n, str):
        return n + "1"
    elif isinstance(n, list):
        return n + [1]
    else:
        return n
    
class MyStr(str):
    def __add__(self,other):
        return self + other + "1"
    def isPlandome(self):
        return self == self[::-1]

s = MyStr("laval")
print(s.isPlandome())