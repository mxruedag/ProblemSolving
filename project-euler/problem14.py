collatzDict = {}

def collatz(n):
    if n == 1:
        collatzDict[1] = 0
    elif n in collatzDict:
        return collatzDict[n]
    elif n%2 == 0:
        collatzDict[n] = collatz(n/2) + 1
    else:
        collatzDict[n] = collatz(3*n+1) + 1
    return collatzDict[n]

maxval = 0
for n in xrange(1,1000000):
    if collatz(n) > maxval:
        maxval = collatz(n)
        ans = n
