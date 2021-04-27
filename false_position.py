#!/usr/bin/env python
import math
import sys

# Finding roots of f(x) using false postion method

f  = lambda x :float(x*x + 2*x + 1)  # f(x) = 0
#f_ = lambda x : float(2*x + 2)

def false_position(p_, p, n): 
    print('Po = ',p_)  
    print('P1 = ',p)
    for _ in range(n):
    
        try:
            y_=f(p_) 
            y=f(p) 
        except:
            print("The values must be in range")
            sys.exit(1)
        if y == 0:
            print(p)
            sys.exit(1)
        t = p 
        p = p - y * (p-p_) / (y-y_)
        if f(t)*f(p_) > 0:    
            p_ = t 
        #print(f"P{_+2} = ")   
    print(p)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        p0 = float(input('Enter Po: '))
        p1 = float(input('Enter P1: '))
        n = int(input('number of iterations: '))
    else:
        p0 = float(sys.argv[1])    
        p1 = float(sys.argv[2])
        n = int(sys.argv[3])
    false_position(p0, p1, n)
