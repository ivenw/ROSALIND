import math
from fastaImport import *

def commonString(list_of_strings, shortest_string, substring_length) :

	'''Finds and returns a common string of set length in a list of strings.
	If no common string is found returns None'''

	#iterate over all possible substrings of set length in the shortest string
	for pos in range(len(shortest_string) - substring_length + 1) :
		substring = shortest_string[pos:pos + substring_length]
		for string in list_of_strings :
			if substring not in string :
				pass
		else :
			return substring
	else :
		return ''


def findSharedMotif(seq_dict) :

	'''Takes dict with sequences as input and returns a longest common substring of the collection'''

	seq_list = list( seq_dict.values() )	#turn dict to list

	seq_list = sorted(seq_list, key=len)		#sort the list ascending by sequence length

	shortest_seq = seq_list.pop(0)		#extract the shortest sequence

	shortest_seq_len = len(shortest_seq)

	left = 0
	right = shortest_seq_len + 1

	while left + 1 < right :
		mid = math.floor((left + right) / 2)

		if commonString(seq_list, shortest_seq, mid) != '' :
			left = mid
		else :
			right = mid
	return commonString(seq_list, shortest_seq, left)

file = 'test_input.txt'

print(findSharedMotif(fastaImport(file)))
