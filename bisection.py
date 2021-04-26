import math
import sys 

CONST = -0.5307963268 

f1 = lambda x : x - 2 * math.sin(x)
f2 = lambda x : x * x * x - 25
f3 = lambda x : x * x * x + x - 4
f  = lambda x : CONST + math.asin(x) + x * math.sqrt(1-x * x)

def bis(a,b,n):
    c = 0
    for _ in range(n):
        c = (a+b)/2
        y1=f(a) # why? not used!
        y2=f(b)
        y3=f(c)
        if y3 > 0:
            b = c
        else:
            a = c
    print(c)
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        a = float(input('put a: \n'))
        b = float(input('put b: \n'))
        c = int(input('put c: \n'))
    else:
        a = float(sys.argv[1])    
        b = float(sys.argv[2])    
        c = int(sys.argv[3])    
    bis(a,b,c)    