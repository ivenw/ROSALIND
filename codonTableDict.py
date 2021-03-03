def codonTableDict() :

	'''takes the data stored in codonTable.txt and returns a dict of the table'''

	fCodon = open('codonTable.txt', 'r')
	CodonStr = fCodon.read()
	fCodon.close()

	CodonStr = CodonStr.replace(' ', '').replace('\n', '')

	codonTable = {CodonStr[i:i+3]: CodonStr[i+3] for i in range(0, len(CodonStr) - 3, 4)}

	return codonTable
