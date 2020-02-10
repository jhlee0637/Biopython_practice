from Bio.Seq import Seq
mRNA = Seq("AUGAACUAAGUUUAGAAU")
ptn = mRNA.translate()
print (ptn)
for seq in ptn.split("*"):
    print (seq)