from Bio.Seq import Seq
seq = Seq("AAGTGACAGGGATTG")
trnsb_seq = seq.transcribe()
trnsl_seq = trnsb_seq.translate(to_stop=True)
print (trnsl_seq)