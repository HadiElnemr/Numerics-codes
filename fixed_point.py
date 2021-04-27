#!/usr/bin/env python
import math
import sys 

# Finding roots of f(x) using Newton's method

g  = lambda x :float(x*x + 3*x + 1)  # f(x) = 0

def fixed_point(p, n): 
    print('Po = ',p)
    for _ in range(n):
        try:
            y=g(p) 
        except:
            print("The values must be in correct range") 
            sys.exit(1)
        if y == 0:
            print(p)
            sys.exit(1)
        print(f'P{_+1} = {p}') 
        p = y
    print(p)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        p = float(input('Enter Po: '))
        n = int(input('number of iterations: '))
    else:
        p = float(sys.argv[1])
        n = int(sys.argv[2])
    fixed_point(p, n)
