from fastaImport import *
import sys

def overlapGraph(k, file) :
	'''Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
	Return: The adjacency list corresponding to substring length k.'''

	fasta_dict = fastaImport(file)

	for key1, string1 in fasta_dict.items() :
		# print(key1)
		suffix = string1[-k:-1] + string1[-1]
		# print(suffix)
		for key2, string2 in fasta_dict.items() :
			# print(key2)
			if key1 == key2 :
				continue
			elif string1 == string2:
				continue
			prefix = string2[:k]
			# print(prefix)
			if suffix == prefix :
				print(f'{key1} {key2}')

print(sys.version)
file = 'test_input.txt'
overlapGraph(3, file)
