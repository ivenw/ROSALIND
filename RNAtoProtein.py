def RNAtoProtein(file) :

	'''converts RNA string to protein sequence in one letter code.
	accepts file with RNA sequence as input.
	returns file with translated sequence'''

	#importing codon table and generating dict
	fCodon = open('codonTable.txt', 'r')
	CodonStr = fCodon.read()
	fCodon.close()

	CodonStr = CodonStr.replace(' ', '').replace('\n', '')

	codonTable = {CodonStr[i:i+3]: CodonStr[i+3] for i in range(0, len(CodonStr) - 3, 4)}

	#converting RNA to protein
	fRNA = open(file, 'r')
	RNAstr = fRNA.read()
	fRNA.close()

	chunkList = [RNAstr[i:i+3] for i in range(0, len(RNAstr) - 2, 3)]

	outTrans = ''.join([codonTable[i] for i in chunkList if codonTable[i] != 'X'])

	print(outTrans)


RNAtoProtein('testInput.txt')
