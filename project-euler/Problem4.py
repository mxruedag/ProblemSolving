def is_palindrome(n):
    strn = str(n)
    if len(strn) <= 1:
        return True
    noLastOrFirst = strn[1:-1]
    return strn[0] == strn[-1] and is_palindrome(noLastOrFirst)

max_pal = 0
for i in xrange(1000):
    for j in xrange(i,1000):
        new = i*j
        if is_palindrome(new) and max_pal < new:
            max_pal = i*j

print max_pal
