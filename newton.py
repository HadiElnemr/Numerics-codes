#!/usr/bin/env python
import math
import sys

# Finding roots of f(x) using Newton's method

f  = lambda x :float(x*x + 2*x + 1)  # f(x) = 0
f_ = lambda x : float(2*x + 2)

def newton(p, n):
    print('Po = ',p)
    for _ in range(n):
        
        try:
            y=f(p) 
            y_=f_(p) #f'(x)
        except:
            print("The values must be in range") 
            sys.exit(1)
        if y == 0:
            print(p)
            sys.exit(1)
        p=p-y/y_
        print(f'P{_+1} = {p}')   
    print(p)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        p = float(input('Enter Po: '))
        n = int(input('number of iterations: '))
    else:
        p = float(sys.argv[1])
        n = int(sys.argv[2])
    newton(p, n)

