>>> from Bio import Entrez
>>> Entrez.email = "Abhishek abhishek.twr@gmail.com"
>>> handle = Entrez.egquery(term = "cortisol")
>>> record = Entrez.read(handle)
>>> for row in record["eGQueryResult"]: print row["DbName"], row["Count"]

pubmed 74012
pmc 12689
journals 0
mesh 28
books 510
omim 79
omia 0
ncbisearch 0
nuccore 188
nucgss 0
nucest 2499
protein 257
genome 0
structure 32
taxonomy 0
snp 19
gene 133
unigene 2
cdd 3
domains 13
unists 3
popset 0
geo 12488
gds 137
homologene 1
cancerchromosomes 0
pccompound 101
pcsubstance 230
pcassay 1192
nlmcatalog 339
gensat 0
probe 1
genomeprj 0
gap 6
proteinclusters 0
>>> 
