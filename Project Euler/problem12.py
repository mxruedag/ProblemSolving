def num_divisors(n):
    ans = 0
    sqrtn = n**0.5
    d = 1
    while d < sqrtn:
        if n%d == 0:
            ans += 2
        d += 1
    if int(sqrtn) - sqrtn < 0.000001:
        ans += 1
    return ans

count = 1
triang = 1

notFound = True

while notFound:
    count += 1
    triang += count
    if num_divisors(triang) > 500:
        n = triang
        notFound = False

print n
