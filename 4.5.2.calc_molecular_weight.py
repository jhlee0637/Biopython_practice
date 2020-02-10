from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import molecular_weight
seq1 = Seq("ATGCAGTAG")
seq2 = Seq("ATGCAGTAG", IUPAC.unambiguous_dna)
seq3 = Seq("ATGCAGTAG", IUPAC.protein)
print(molecular_weight(seq1))
print(molecular_weight(seq2))
print(molecular_weight(seq3))