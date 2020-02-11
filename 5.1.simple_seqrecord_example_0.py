from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
seq = Seq("ACGT")
seqRecord = SeqRecord(seq)
seqRecord.name = "example_name"
seqRecord.id = "example_ID"
seqRecord.description = "example_des"
seqRecord.features = "111111111"
print (seqRecord)