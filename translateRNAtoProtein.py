def translateRNA(s) :

	'''Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
	Return: The protein string encoded by s.'''

	#Test if input is legal
	if type(s) is not str :
		return('Input is not str')

	if len(s) > 10000 :
		return('Input too long. Max 10 kbp')

	if len(s) / 3 != int :
		return('Input not divisble by three')

	s = s.upper()

	RNA = ('A', 'C', 'G', 'U')

	for i in s :
		if i not in RNA :
			return('Input not a RNA sequence')

	#Actual function
	codonTable = {}

	for
