import math
def f1(x):
    return x-2*math.sin(x)
def f2(x):
    return x*x*x-25
def f3(x):
    return x*x*x+x-4
def f(x):
    return -0.5307963268 + math.asin(x) + x*math.sqrt(1-x*x)

def bis(a,b,n):
    c = 0
    for i in range(0,n):
        c = (a+b)/2
        y1=f(a)
        y2=f(b)
        y3=f(c)
        if y3 > 0:
            b = c
        else:
            a = c
    print(c)
    
bis(float(input('put a\n')), float(input('put b\n')),int(input('put n\n')))
