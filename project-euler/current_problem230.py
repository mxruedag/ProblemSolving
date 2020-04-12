def fib_through(list_fib, n):
    """
    Returns a list with two values, the n-1-th and the n-th fibonacci, where the
    starting values are the two items in list_fib.
    Mutates the list provided
    """
    for i in range(n-2):
        list_fib = [list_fib[-1], list_fib[-1] + list_fib[-2]]
    return list_fib

# def compute(A, B, n):
#     length_fib = [len(A), len(B), len(A) + len(B)]
#     if n-1 < len(A):
#         return A[n-1]
#     if n-1 < len(B):
#         return B[n-1]
#     iterations = 0
#     while length_fib[2] < n:
#         length_fib = [length_fib[-2], length_fib[-1], length_fib[-2]+length_fib[-1]]
#         iterations += 1
#     idx = n
#     while iterations > 0:
#         if idx > length_fib[0]:
#             idx = idx - length_fib[0]
#         else:
#             length_fib = [length_fib[1] - length_fib[0], length_fib[0], length_fib[1]]
#             iterations -= 1
#         length_fib = [length_fib[1] - length_fib[0], length_fib[0], length_fib[1]]
#         iterations -= 1
#     if idx - 1 < len(A):
#         return A[idx - 1]
#     return B[idx - len(A) - 1]

def compute(A, B, n):
    iterations = 0
    fib = [len(A), len(B)]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    # If the length of fib is even, the last one begins with B
    # If the length of fib is odd, the last one begins with A
    # Invariant: we're looking for the idx-th digit of the string rep by fib[-1]
    idx = n - 1
    while len(fib) > 2:
        if (len(fib) % 2 == 0) and (idx < len(B)):
            return B[idx]
        if (len(fib) % 2 == 1) and (idx < len(A)):
            return A[idx]
        if fib[-2] > idx:
            fib.pop(-1)
            fib.pop(-1)
        else:
            idx -= fib[-2]
            fib.pop(-1)
    

if __name__ == '__main__':
    num_inps = input()
    num_inps = int(num_inps)
    for i in range(num_inps):
        inp = input()
        A, B, n = inp.split(' ')
        n = int(n)
        print(compute(A, B, n))
