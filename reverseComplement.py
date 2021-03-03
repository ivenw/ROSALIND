from importNT import *

def reverseComplement(s) :

	'''Given: A DNA string s of length at most 1000 bp.
	Return: The reverse complement sc of s.'''

	if type(s) != str :
		return('Input not str')

	if len(s) > 1000 :
		return('Input too long.')

	s = s.upper()

	DNA = ('A', 'C', 'G', 'T')

	if (any(map(lambda i : i not in DNA, s))) :
		return('Input not a DNA sequence')

	key = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

	return ''.join([key[i] for i in reversed(s)])

fin = 'input/rosalind_revc.txt'

fout = open('input/roslaind_revc_out.txt', 'w+')

fout.write(reverseComplement(importNT(fin)))
