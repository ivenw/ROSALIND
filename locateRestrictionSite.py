from fastaImport import *
from reverseComplement import *

def locateRestrictionSite(file) :

	'''takes file with dna string in fasta format and returns prints position
	and length of every reverse palindrome in the string of length 4-12.'''

	DNA_string = next( iter( fastaImport(file).values() ) )

	isPali = lambda str: str == reverseComplement(str)	#function for checking if str is a reverse palindrome

	positions = []

	for i in range (4, 13) :
		for c in range(0, len(DNA_string) - i + 1) :
			chunk_str = DNA_string[c:c+i]
			if isPali(chunk_str) :
				positions.append([c, i])

	positions.sort()

	with open('output.txt', 'w') as out_file :
		[ out_file.write(f'{x[0]+1} {x[1]}\n') for x in positions ]
		out_file.close()

locateRestrictionSite('testInput.txt')
