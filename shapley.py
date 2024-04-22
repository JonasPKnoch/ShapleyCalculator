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

def powerSetContaining(s, i):
    exclude = s[i]
    remaining = s[:i] + s[i + 1:]
    pow = powerSet(remaining)
    for p in pow:
        p.append(exclude)
    
    return pow


def shapley(n, i, v):
    players = list(range(n))
    sum = 0
    nFac = math.factorial(n)
    pi = powerSetContaining(players, i)
    for s in pi:
        sSize = len(s)
        sumEl = v(s) - v(s[:-1])
        sumEl *= math.factorial(sSize - 1)*math.factorial(n - sSize)/nFac
        sum += sumEl
    
    return sum

def v(s):
    if len(s) < 9:
        return 0
    for i in range(5):
        if i not in s:
            return 0
    return 1

print(shapley(15, 8, v))