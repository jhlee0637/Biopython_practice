from Bio.Seq import Seq
mRNA = Seq("AUGAACUAAGUUUAGAAU")
ptn =  mRNA.translate(to_stop=True)
print (ptn)
