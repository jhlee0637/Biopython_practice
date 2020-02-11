from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
simple_seq = Seq("ACGT")
simple_seqRecord = SeqRecord(simple_seq, id="NC_1111", name="Test")
print(simple_seqRecord)