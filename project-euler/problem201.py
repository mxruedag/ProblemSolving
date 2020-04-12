def subsets_of_size(s, m):
	"""
	Gets a list of all the subsets of s of size m 
	"""
	if m == 0:
		return [set()]
	if len(s) == m:
		return [set(s)]
	ans = []
	sorted_set = sorted(s)
	return subsets_of_size(s[1:], m) + [subset.union([s[0]]) for subset in subsets_of_size(s[1:], m-1)]

def sums_of_subsets(s, m):
	"""
	Gets the counts of the sums of all the subsets of s of size m 
	"""
	if len(s) == m:
		return {sum(s): 1}
	if m == 1:
		ans = {}
		for elt in s:
			if elt in ans:
				ans[elt] += 1
			else:
				ans[elt] = 1
		return ans
	ans = []
	elt = s[0]
	sums_without_elt = sums_of_subsets(s[1:], m)
	sums_with_elt = sums_of_subsets(s[1:], m-1)
	ans = sums_without_elt.copy()
	for k, v in sums_with_elt.items():
		if k+elt in ans:
			ans[k+elt] += v
		else:
			ans[k+elt] = v
	return ans

def sums_of_subsets_2(s, m, i, ans):
	"""
	Gets the counts of the sums of all the subsets of s[i:] of size m
	and stores it in ans[(m, i)].
	"""
	if (m,i) in ans:
		return ans[(m, i)]
	if m == len(s)-i:
		ans[(m, i)] = {sum(s[i:]): 1}
		return ans[(m, i)]
	if m == 1:
		ans[(m, i)] = {}
		for idx in range(i, len(s)):
			if s[idx] in ans[(m, i)]:
				ans[(m, i)][s[idx]] = None
			else:
				ans[(m, i)][s[idx]] = 1
		return ans[(m, i)]
	ans[(m,i)] = sums_of_subsets_2(s, m, i+1, ans).copy()
	for k, v in sums_of_subsets_2(s, m-1, i+1, ans).items():
		if v == None or (k+s[i] in ans[(m, i)]):
			ans[(m, i)][k + s[i]] = None
		else:
			ans[(m, i)][k + s[i]] = v
	return ans[(m, i)]


def main_hackerrank():
	n_and_m = input()
	n, m = int(n_and_m.split(' ')[0]), int(n_and_m.split(' ')[1])
	set_elts = input()
	s = list(map(int, set_elts.split(' ')[:n]))
	ans = {}
	sums = sums_of_subsets_2(s, m, 0, ans)
	return sum([k for k, v in sums.items() if v == 1])

def main():
	s = [a**2 for a in range(1, 101)]
	ans = {}
	sums = sums_of_subsets_2(s, 50, 0, ans)
	return sum([k for k, v in sums.items() if v == 1])
