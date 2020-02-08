from Bio.Seq import Seq

exon_seq = Seq("ATGCAGTAG")
count_a = exon_seq.count("A")
print (count_a)