from fastaImport import *

def findSharedMotif(seq_dict) :
	'''takes dict with sequences as input and returns a longest common substring of the collection'''

	seq_list = list( seq_dict.values() )

	seq_list = sorted(seq_list, key=len)

	shortest_seq = seq_list.pop(0)

	shortest_seq_len = len(shortest_seq)

	for chunk_size in range(shortest_seq_len, 0, -1) :
		for pos in range(shortest_seq_len - chunk_size + 1) :
			chunk = shortest_seq[pos:pos + chunk_size]
			for seq in seq_list :
				if chunk not in seq :
					break
			else :
				return chunk

file = 'test_input.txt'

print(findSharedMotif(fastaImport(file)))
