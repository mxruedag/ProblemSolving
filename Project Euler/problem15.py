def sum_digits(n):
    ans = 0
    for i in str(n):
        ans += int(i)
    return ans
