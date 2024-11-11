class Calcul:
    def __init__(self): # Constructeur par défaut
        pass

    def factorielle(self, n):
        f = 1
        for i in range(1,n+1):
            f *= i
        return f
    
    def factorielle2(self,n): # n! = n * (n-1)!
        if n <= 1 :
            return 1
        return n * self.factorielle2(n-1)
    
    def somme(self,n:int)->int:
        s = 0
        for i in range(1,n+1):
            s += i
        return s
    def isPrim(self,n:int)->bool:
        for i in range(2,n//2):
            if n % i == 0 :
                return False
        return True
    def isPrims(self,a,b):
        for i in range(2,min(a,b)):
            if a%i==0 and b%i==0:
                return False
        return True
    def tableMult(self,n):
        print(f"la table de multiplication de {n} :")
        for i in range(1,11):
            print(f"{n} * {i} = {n*i}")
    
    def allTableMult(self):
        for i in range(1,10):
            self.tableMult(i)

    def listDiv(self,n:int)->list:
        L = []
        for i in range(1,n):
            if n%i==0:
                L.append(i)
        return L
    
    def listDivPrim(self,n):
        L = []
        for i in range(1,n):
            if n%i==0 and self.isPrim(i)==True:
                L.append(i)
        return L
    

calcul = Calcul()
print(calcul.factorielle(6))
print(calcul.factorielle2(6))
calcul.allTableMult()
print(calcul.listDiv(100))
print(calcul.listDivPrim(100))

