from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

tatabox_seq = Seq("tataaaggcAATATGCAGTAG", IUPAC.unambiguous_dna)
print(tatabox_seq)
print(type(tatabox_seq))