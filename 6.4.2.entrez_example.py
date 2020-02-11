from Bio import Entrez
Entrez.email = "jhlee0637@gmail.com"
handle = Entrez.efetch(db="nucleotide", rettype="gb", id="AY463215", retmode="text")
for s in handle:
    print (s.strip())