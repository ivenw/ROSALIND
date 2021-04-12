from itertools import permutations

def enumerateGeneOrder(n) :
	'''Given: A positive integer n≤7
	Return: The total number of permutations of length n,
	followed by a list of all such permutations (in any order).
	'''
	sequence = [x+1 for x in range(n)]

	perm_list = list(permutations(sequence, n))

	print(len(perm_list))

	for a in perm_list :
		out_str = ''
		for i in a :
			if i == a[-1] :
				out_str += f'{i}'
			else :
				out_str += f'{i} '
		print(out_str)


print(enumerateGeneOrder(6))
