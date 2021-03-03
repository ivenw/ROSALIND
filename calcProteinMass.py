import pandas as pd

def calcProteinMass(file) :

	'''calculates mass of protein sequence.
	accepts file with single letter protein sequence.
	returns total mass.'''

	massDict = dict( pd.read_csv('monoisotopic_mass.txt', header=None).values)

	f = open(file, 'r')
	fStr = f.read()
	f.close()

	fStr = fStr.replace('\n', '')

	mass = 0.0

	for i in fStr :
		mass += massDict[i]

	return mass

print(calcProteinMass('testInput.txt'))
