import itertools

def all_strings(in_file, out_file) :
	'''Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n
 	(n10)

	Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).'''

	with open(in_file) as input :
		lex = input.readline().replace('\n', '').replace(' ', '')
		n = int(input.readline().replace('\n', ''))
		input.close()

	out = itertools.combinations_with_replacement(lex, n)

	out_str_list = []
	for i in out :
		out_str = ''
		for s in i :
			out_str += str(s)
		out_str_list.append(out_str)

	with open(out_file, 'w') as output :
		[output.write(str(x)+' ') for x in out_str_list]
	output.close()

all_strings('input.txt', 'output.txt')
