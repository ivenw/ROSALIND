def wascallyWabbits(n, k, m) :

	'''Returns the number of rabbit pairs after n months with dying after m months + k litter pairs per month per pair'''

	memo = {}
	memo[0], memo[1] = 1, 1

	for i in range(2, n) :
		if i < m or m == 0:
			memo[i] = memo[i-2] * k + memo[i-1]
		elif i == m:
			memo[i] = (memo[i-2] * k) + memo[i-1] - memo[i-m]
		else :
			memo[i] = (memo[i-2] * k) + memo[i-1] - memo[i-m-1]

	return memo[n-1]

print(wascallyWabbits(5, 1, 0))
