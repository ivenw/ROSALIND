from fastaImport import *

def findSharedMotif(seq_dict) :
	'''takes dict with sequences as input and returns a longest common substring of the collection'''



file = '/Users/ivenwinkelmann/Downloads/rosalind_subs.txt'

print(findSharedMotif(fastaImport(file)))
