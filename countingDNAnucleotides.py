def DNAcount(s) :

	'''Given: A DNA string s of length at most 1000 nt.

	Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.'''

	if type(s) != str :
		return ('Input not a str')

	if len(s) > 1000 :
		return ('String too long. Max 1000 nt.')

	return (str(s.count('A')) + ' ' + str(s.count('C')) + ' '
	+ str(s.count('G')) + ' ' + str(s.count('T')))

print(DNAcount('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))

x = 'AACCACGTCGATGCCACCGCAAACAAAGGATCGCGTCGACTCGGAGCTGCCCAACTGTGAGCCGTAGCGTTAAGCGCCGCGAAACTATTGGGAAGTACCTACAGTAAAGCCATGGCCATTGGACGCCAGCCAGCTTCTTCTATGTTTAGTGAAGAAAAGTGCTTTTGGTGCGAGAGTTTAATGTATTCGCCTAGGAGAGGCGTCCCCGGAATCGGCACGCCATGATGTAAGGAGAAGGCCGTAACATTGATGAGTAAAGGGGTCAATCGCATCCGCAGCTTCATCGCCTATGTCGATCCGTGGCATATTCATCTCCGTGTATTGCTTGCGCCCATATGAAGCAGGATCTTGAAGTAGGTTTAGGTGCGCCGACTGCATAGTCCCAATAAAGGAGGTTCGTTGGTGCCCGTGTAGTATATGAGGTGCTACTTTCCACATGTTAACCTTTCTGTTCTTGTCCGGAGAGCATTGCCCAGGGCCCATTCCCGGGCAGTATTGGAATTAATCGGGAATGTACCCCTCTTGTACCTACTAGCGTCGTCGAATGATATCAAAGAGCAGTAAAATAGCCAGCACTGAGAGAACCTACCGTTTGTGTACCGCTTCCAACTAGTATAAGATCTCTAGAAGATTCAATATCTTTCCATGACGCGTCACGTAGGCGTCCTGGAAGCCTCTAAGAACTTCCAGCGATATGGAGGTGCTATAAGGTCGCACATACTAGTAGAGCAGCAATTGACGGGTCCCCGTGTCAAAACATATTACCAAAAGGTGGCGAAGAATCGGCTCACCTAATTGAGAATTCTTCGTCCCAGGACGAGGCGATGTTATCCTAAACATCGTACTCTCTGATCCCACGGGGGGCTGTACGAGTAGAGGAACTGTCACGTCGGACCCTTACGCGCTGAGGTGACTTTCC'

print(DNAcount(x))
