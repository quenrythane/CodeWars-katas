"""
A perfect power is a classification of positive integers:

In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive
integer. More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that m^k = n.

Your task is to check wheter a given integer is a perfect power. If it is a perfect power, return a pair m and k with
m^k = n as a proof. Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.

Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid
solutions. However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.

Examples
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None
"""


def isPP2(n):
    x = int(n ** (1/2) + 2)
    for k in range(2, x):
        for m in range(2, x):
            if m ** k == n:
                return [m, k]


from math import ceil, log, sqrt
def isPP(n):
    for b in range(2, int(sqrt(n)) + 1):
        e = int(round(log(n, b)))
        if b ** e == n:
            return [b, e]
    return None


def isPP3(n):
    x, y = 2, 2
    while x**2 <= n:
        if x**y == n:
            return[x,y]
        if x**y > n:
            x+=1
            y = 1
        y+=1
    return None


from math import log
def isPP4(n, e=1e-12):
    for p in range(2, int(log(n, 2)) + 1):
        if int(n ** (1./p) + e) ** p == n:
            return [int(n ** (1./p) + e), p]


def isPP5(n):
    for exponent in range(2,8):
        root = n ** (1.0/exponent)
        if int(round(root)) ** exponent == n:
            return [int(round(root)), exponent]


print(isPP(8))
print(isPP(4))
print(isPP(343))
print(isPP(5489031744))
print(isPP(8000000))
print(isPP2(8000000))
