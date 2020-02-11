from Bio import Entrez
from Bio import SeqIO

Entrez.email= "jhlee0637@gmail.com"

with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="1575550") as handle:
    seq = SeqIO.read(handle, "fasta")

print (seq)
print (len(seq))