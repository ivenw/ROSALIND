from fastaImport import *

def gcContent(file) :

	'''computes GC content of DNA strings in fasta format.
	accepts file with DNA strings in fasta format as input.
	print unrounded GC content '''

	inputDict = fastaImport(file)

	testDict = {}

	for key, value in inputDict.items() :
		GCperc = (value.count('G') + value.count('C')) / len(value) * 100
		testDict[key] = GCperc

	print(max(testDict, key = testDict.get))
	print(max(testDict.values()))

gcContent('testInput.txt')
