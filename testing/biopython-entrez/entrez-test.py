from Bio import Entrez
Entrez.email = "zadaum10@gmail.com"
handle = Entrez.esearch(db="pubmed", term="Yang Y[Author] AND Affiliated Hospital of Jining Medical University[Affiliation]")
record = Entrez.read(handle)
print(record["IdList"])
