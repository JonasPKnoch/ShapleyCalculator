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

numPermMembers = 5
numNPermMembers = 10
permVetoCount = 1
nPermVetoCount = 99999
winVotes = 9

def v(s):
    if len(s) < 9:
        return 0
    for i in range(5):
        if i not in s:
            return 0
    return 1

def vModified(s):
    permVotes = 0
    for i in range(0, numPermMembers):
        if i in s:
            permVotes += 1
    permVetos = numPermMembers - permVotes

    nPermVotes = 0
    for i in range(numPermMembers, numPermMembers + numNPermMembers):
        if i in s:
            nPermVotes += 1
    nPermVetos = numPermMembers - nPermVotes

    if permVetos >= permVetoCount:
        return 0
        
    if nPermVetos >= nPermVetoCount:
        return 0
        
    if permVotes + nPermVotes < winVotes:
        return 0
    
    return 1

print(shapley(numPermMembers + numNPermMembers, 0, vModified) * 100)
print(shapley(numPermMembers + numNPermMembers, 5, vModified ) * 100)

for s in powerSet(list(range(15))):
    break
    v1 = v(s)
    v2 = vModified(s)
    if v1 != v2:
        print(str(s) + ": " + str(v1) + " " + str(v2))