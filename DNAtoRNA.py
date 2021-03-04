def DNAtoRNA (t) :

	'''Given: A DNA string t having length at most 1000 nt.
	Return: The transcribed RNA string of t.'''

	if type(t) != str :
		return ('Input not str')

	if len(t) > 1000 :
		return ('Input too long')

	u = ''

	t = t.upper()

	return t.replace('T', 'U')
