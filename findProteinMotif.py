from importUniprot import *
from pmotifParse import *

def findProteinMotif(seqs, motif) :

	'''takes seqs with UniProt IDs and returns positions of glycosilation motif for each entry'''

	def ismotif (seq, motif, start) :
		count = 0
		for i in range(len(seq) - len(motif) - start) : #iterate over sequence index
			test = []
			for m in range(len(motif)) :
				if seq[start + i + m] in motif[m] : #check if m position of motif is fullfilled
					test.append(True)
				else:
					for r in range(len(motif) - m) :
						test.append(False)
					break

			if all(test) is True :
				return i + start
			elif i == (len(seq) - len(motif) - start - 1) : #if motif can't be found, return -1
				return -1
			else :
				test = []

	def motifPos(seq, motif) :
		index = 0
		out = []
		skip_old = 0
		skip_new = 0
		count = 0
		for i in range(len(seq)) :
			while count > 0 :
				count -= 1
				continue
			else :
				if ismotif(seq, motif, index) == -1 :
					break
				else:
					index = ismotif(seq, motif, index) + 1
					out.append(str(index))
					skip_old = skip_new
					skip_new = index - skip_old
					count = skip_new
		return ' '.join(out)


	return motifPos(seqs, motif)

def findMotifList(file) :
	with open(file, 'r', encoding='utf-8') as response :
		list = response.readlines()

	for i in list :
		print(i.replace('\n', ''))
		print(
		findProteinMotif(importUniprot(i.replace('\n', '')), pmotifParse('N{P}[ST]{P}'))
		)

findMotifList('testInput.txt')
