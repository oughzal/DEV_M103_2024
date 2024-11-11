from multipledispatch import dispatch
@dispatch(int,int)
def func(a:int,b:int)->int: return 1
@dispatch(int,float)
def func(a:int,b:float)->int: return 2

@dispatch(float,int)
def func(a:float,b:int)->int: return 6
@dispatch(float,int)
def func(a:float,b:int)->str: return 7
@dispatch(int)
def func(a:int)->int: return 3
@dispatch(int,int,int)
def func(a:int,b:int,c:int)->int: return 4
@dispatch(int,int,float)
def func(a:int,b:int,c:float)->str: return 5

print(func(4.0,5))