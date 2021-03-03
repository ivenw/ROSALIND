from codonTableDict import *
from collections import Counter

def inferRNAfromProtein(file) :

	'''takes a file with string of protein sequence and returns the total number
	of different mRNA strings the protein could have been translated from
	expressed as mod 1.000.000'''

	with open(file, 'r') as f :
		protein_str = f.read().replace('\n', '')
		f.close()

	codon_table = codonTableDict()	#importing codon table

	codon_count = Counter(codon_table.values()) #number of codons per amino acid

	possible_RNA = 1

	for residue in protein_str :
		possible_RNA *= codon_count[residue]

	possible_RNA *= codon_count['X']

	return possible_RNA % 1000000

print(inferRNAfromProtein('testInput.txt'))
