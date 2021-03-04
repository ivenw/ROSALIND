from fastaImport import *
from DNAtoRNA import *
from RNAtoProtein import *

def RNAsplicing(file) :

	'''Takes a file with DNA strings in fasta format. First sequence is the DNA
	sequence and subsequent sequences are introns.
	Returns protein string translated from the resulting mRNA.'''

	fasta_list = list(fastaImport(file).values())

	cDNA = fasta_list[0]

	for i in fasta_list[1:] :
		cDNA = cDNA.replace(i, '')

	pseq = RNAtoProtein( DNAtoRNA(cDNA) )

	with open('output.txt', 'w') as out_file :
		out_file.write(pseq)
		out_file.close()

RNAsplicing('test_input.txt')
