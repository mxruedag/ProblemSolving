def compute(n_values):
    """
    Gets the sorted list of primes less than n
    """
    places_of_n_values = {n: i for i,n in enumerate(n_values)}
    n_values_sorted = sorted(n_values)
    current_n_index = 0
    largest_n = max(n_values)
    ans_sums = []
    final_ans = [None for i in range(len(n_values))]
    list_of_primes = [2]
    # For each key, the number of subsets of S that add to it
    subsets_adding_to = {2: 1}
    max_sum = 2
    p = 3
    while p <= largest_n or p <= max_sum:
        for d in list_of_primes:
            if d**2 > p:
                list_of_primes.append(p)
                if p <= largest_n:
                    new_subsets_adding_to = {p : 1}
                    new_subsets_adding_to.update({p+s : 1 for s in subsets_adding_to})
                    for s in new_subsets_adding_to:
                        if s not in subsets_adding_to:
                            subsets_adding_to[s] = 1
                        else:
                            subsets_adding_to[s] += 1
                    max_sum = max_sum + p
                break
            if p % d == 0:
                break
        if current_n_index < len(n_values) and p == n_values_sorted[current_n_index] - 1:
            ans_sums.append(subsets_adding_to.copy())
            current_n_index += 1
        p += 1
    for i, ans_sum in enumerate(ans_sums):
        prime_sums = set(ans_sum).intersection(set(list_of_primes))
        total_sums = sum([ans_sum[prime_sum] for prime_sum in prime_sums])
        final_ans[places_of_n_values[n_values_sorted[i]]] = total_sums % 10**16
    return list_of_primes, final_ans

if __name__ == '__main__':
    k = input()
    k = int(k)
    n_values_str = input()
    n_values_list = n_values_str.split(' ')
    n_values_list = [int(n) for n in n_values_list][:k]
    answers = compute(n_values_list)
    print(' '.join([str(a) for a in answers]))
