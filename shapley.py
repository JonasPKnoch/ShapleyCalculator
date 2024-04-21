import math

def powerSet(set):
    if len(set) == 1:
        return [set, []]
    
    first = set[0]
    pow = powerSet(set[1:])
    halfN = len(pow)
    for i in range(halfN):
        pow.append(pow[i] + [first])
    
    return pow

def powerSetContaining(set, i):
    exclude = set[i]
    remaining = set[:i] + set[i + 1:]
    pow = powerSet(remaining)
    for p in pow:
        p.append(exclude)
    
    return pow


def shapley(n, v):
    players = list(range(n))
    sum = 0
    nFac = math.factorial(n)
    for i in range(len(set)):
        s = powerSetContaining(set, i)
        sSize = len(s)
        sumEl = v(s) - v(s[:-1])
        sumEl *= math.factorial(sSize - 1)*math.factorial(n - sSize)/nFac
