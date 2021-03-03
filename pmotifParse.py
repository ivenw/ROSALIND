def pmotifParse (motif):

	'''takes a protein motif (str) and returns list with legal characters that
	can be iteratet on'''

	aa = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F',
	'P', 'S', 'T', 'W', 'Y', 'V']
	out = []
	skip = 0
	for i in range(len(motif)) :
		if skip > 0 :
			skip -= 1
			continue

		#check for is not
		elif motif[i] == '{' :
			exce = []
			allowed = []
			for s in range(len(motif[i:])) :
				if motif[i+s+1] == '}' :
					skip = s + 1
					for a in aa:
						if a in exce :
							continue
						else :
							allowed.append(a)
					out.append(allowed)
					break
				else :
					exce.append(motif[i+s+1])

		#check for is or
		elif motif[i] == '[' :
			allowed = []
			for s in range(len(motif[i:])) :
				if motif[i+s+1] == ']' :
					skip = s + 1
					out.append(allowed)
					break
				else :
					allowed.append(motif[i+s+1])

		else :
			out.append(motif[i])

	return out
