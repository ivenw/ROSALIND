def findDNAmotif(s, t) :
	c = 0
	out = []
	while t in s[c:] :
		i = s.index(t, c) + 1
		c = i
		out.append(str(i))
	else :
		return ' '.join(out)

f = open('/Users/ivenwinkelmann/Downloads/rosalind_subs.txt', 'r')
x = f.readline()
y = f.readline()

print(findDNAmotif(x, y))
