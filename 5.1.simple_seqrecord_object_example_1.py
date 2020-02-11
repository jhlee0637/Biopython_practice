from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
seq = Seq("ACGT")
seqRecord = SeqRecord(seq)
print (seqRecord)