import numpy as np
import random
import math

def integralLatex(i):
    return "\int_{0}^{x}f_{" + i + "}\left(t\\right)dt"

def derivativeLatex(i):
    return "\\frac{d}{dx}f_{" + i + "}\left(x\\right)"

def noteLatex(i, dec=1):
    return f"\operatorname{{tone}}\left(\left(f_{i}\left(p\\right)\\right),\ {dec}\\right)"

def pointLatex(i):
    return "\left(p,b\left(f_{" + str(i) + "}\left(p\\right)\\right)\\right)"


def rootsToPoly(roots):
    return np.poly(roots)*random.randint(1,50)

def dilatePoly(coefficients, k):
    return coefficients*k

def printPoly(coefficients, domain=450):
    i=1
    if type(coefficients) == float: coefficients = [coefficients]

    coefficients = list(coefficients)

    for i in range(len(coefficients)):
        coefficients[i] = f"({coefficients[i]:.{degreeToDilation[len(coefficients)-i-1]*-1 + 1}f})*x^{len(coefficients)-1-i}"
        # print(f"{coef}*x^{len(coefficients)-i}", end=" + ")
        i+=1
    # return ' + '.join(coefficients) + "\left\{{0<x<{domain}\\right\}}"
    return ' + '.join(coefficients)


def creatListWords(degree):
    origrinals = []
    bs = []
    for i in range(5):

        randomRoots = [random.randint(0, 2000) for j in range(1, 8)]
        print(randomRoots)
        poly = rootsToPoly(randomRoots[6 - degree:6])
        dilatedPoly = dilatePoly(poly, math.pow(10, degreeToDilation[degree]))

        origrinals.append(f"f_{i}(x) = {printPoly(dilatedPoly)}")
        bs.append(f"b(f_{i}(x))")

    for func in origrinals: print(func)
    print()
    for b in bs: print(b)
    print()

    for i in range(len(origrinals)): print(noteLatex(i))
    print()
    for i in range(len(origrinals)): print(pointLatex(i))

degreeToDilation = {0:1,
                    1:-1,
                    2:-3,
                    3:-9,
                    4:-9,
                    5:-13,
                    6:-15,
                    7:-17}

creatListWords(5)

