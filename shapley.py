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

numPermMembers = 5 #5
numNonPermMembers = 10 #10
permVetoCount = 1 #1
nonPermVetoCount = 2 #9999
winVotes = 9 #9

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

    NonPermVotes = 0
    for i in range(numPermMembers, numPermMembers + numNonPermMembers):
        if i in s:
            NonPermVotes += 1
    NonPermVetos = numNonPermMembers - NonPermVotes

    if permVetos >= permVetoCount:
        return 0
        
    if NonPermVetos >= nonPermVetoCount:
        return 0
        
    if permVotes + NonPermVotes < winVotes:
        return 0
    
    return 1

permShap = shapley(numPermMembers + numNonPermMembers, 0, vModified) * 100
NonPermShap = shapley(numPermMembers + numNonPermMembers, numPermMembers, vModified ) * 100
print(str(round(permShap, 3)) + "%")
print(str(round(NonPermShap, 3)) + "%")
print(permShap*numPermMembers + NonPermShap*numNonPermMembers)