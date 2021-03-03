def importNT(file):

	'''Takes file path and returns a NT string. Checks for legality of input.
	Removes any trailing white space characters'''

	file = open(file, 'r')

	f = file.read()

	if type(f) != str :
		return('Input not str')

	s = ''

	for i in f :
		if i.isalpha() != True :
			continue
		s += i

	DNA = ('A', 'C', 'G', 'T', 'U')

	if (any(map(lambda i : i not in DNA, s))) :
		return('Input not a DNA or RNA sequence')

	return s

	file.close()
