str1 = "ACGT"
str2 = "ACGT"
print (str1)
print (str2)
print (str1==str2)
print ("----------")
from Bio.Seq import Seq
seq1 = Seq("ACGT")
seq2 = Seq("ACGT")
print (seq1)
print (seq2)
print (seq1 == seq2)
print ("----------")
from Bio.SeqRecord import SeqRecord
record1 = SeqRecord(seq1)
record2 = SeqRecord(seq2)
print (record1)
print (record2)
print (record1.seq == record2.seq)