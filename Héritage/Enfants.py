class Pere:
    x = 5
    def y(self):
        return 6
class Mere:
    x = 7
    def y(self):
        return 8
class Enfant(Mere, Pere):
    pass

e1 = Enfant()
print(e1.x)  # 5
print(e1.y())