''' Muller's Recurrence '''
from decimal import Decimal

def rec(y, z):
    return 108 - ((815-1500/z)/y)

def floatpt(N):
    x = [4, 4.25]
    for i in range(2, N+1):
        x.append(rec(x[i-1], x[i-2]))
    return x

def fixedpt(N):
    x = [Decimal(4), Decimal(17)/Decimal(4)]
    for i in range(2, N+1):
        x.append(rec(x[i-1], x[i-2]))
    return x

N = 20
flt = floatpt(N)
fxd = fixedpt(N)

for i in range(N):
    print(str(i) + ' | ' + str(flt[i]) + ' | ' + str(fxd[i]))




# def f(x, y):
#     return 333.75 * y**6 + (x**2(11 * x**2 * y**2 - y**6 - 121 * y**4 -2) + 5.5 * y**8 + x / 2*y)

# print(str(f(77617, 33096)))
