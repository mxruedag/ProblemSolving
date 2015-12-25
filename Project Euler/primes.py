# Problem 7 

##primes = [2]
##
##is_prime = 3
##
##while len(primes) < 10002:
##    for p in primes:
##        if p**2 > is_prime:
##            primes.append(is_prime)
##            is_prime += 1
##            break
##        elif is_prime%p == 0:
##            is_prime += 1
##            break
##
##print primes[10000]

# Problem 3

##primes3 = [2]
##
##is_prime = 3
##sqrtp = 600851475143**0.5
##
##while primes3[-1] <= sqrtp:
##    for p in primes3:
##        if p**2 > is_prime:
##            primes3.append(is_prime)
##            is_prime += 1
##            break
##        elif is_prime%p == 0:
##            is_prime += 1
##            break
##
##divisors = []
##       
##myNum = 600851475143
##for p in primes3:
##    if myNum%p == 0:
##        divisors.append(p)
##
##print divisors[-1]

# Problem 10

primes3 = [2]

is_prime = 3

while primes3[-1] <= 2000000:
    for p in primes3:
        if p**2 > is_prime:
            primes3.append(is_prime)
            is_prime += 1
            break
        elif is_prime%p == 0:
            is_prime += 1
            break
        
print sum(primes3[:-1])

