from urllib.request import urlopen

def importUniprot(Uniprot_ID) :

	'''Given Uniprot ID str, returns str of protein sequence'''

	with urlopen('https://www.uniprot.org/uniprot/' + Uniprot_ID + '.fasta') as response :
		html_content = response.read()

	encoding = response.headers.get_content_charset('utf-8')
	html_text = html_content.decode(encoding)

	html_text = html_text.split('\n', 1)[1].replace('\n', '')

	return html_text
