import requests
r = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22368089')
r = r.text
n = open("22368089.txt","x")
f = open("22368089.txt","w")
f.write(r)
f.close()
