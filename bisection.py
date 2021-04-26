import math


CONST = -0.5307963268


def f1(x): return x - 2*math.sin(x)
def f2(x): return x*x*x-25
def f3(x): return x*x*x+x-4
def f(x): return CONST + math.asin(x) + x*math.sqrt(1-x*x)


def bis(a, b, n):
    c = 0
    for _ in range(n):
        c = (a+b)/2
        y1 = f(a) # why it's never used?
        y2 = f(b)
        y3 = f(c)
        if y3 > 0:
            b = c
        else:
            a = c
    print(c)

def main():
    bis(float(input('put a\n')), float(input('put b\n')), int(input('put n\n')))

if __name__ == "__main__":
    main()