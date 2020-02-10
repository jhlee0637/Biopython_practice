from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio.SeqUtils import MeltingTemp as mt 
seq = Seq("AAGTGACAGGGATTG")
GC_per = GC(seq)
mt_p = mt.Tm_Wallace(seq)
print (GC_per)
print (mt_p)