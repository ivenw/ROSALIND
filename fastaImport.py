def fastaImport(file) :

	'''given a fasta file, returns all entries as dict'''

	f = open(file, 'r')
	fStr = f.read()	#open file and generate string of contents
	f.close()

	entries = fStr.split('>')	#generate list of entries
	del entries[0]	#remove leading empty entry

	outDict = {}	#init dict for output

	for e in entries :
		entryLst = e.splitlines()
		key = entryLst[0] #extract the future key value
		item = ''
		for part in entryLst[1:] :	#concat all parts of the DNA string
			item += part

		outDict[key] = item

	return outDict
