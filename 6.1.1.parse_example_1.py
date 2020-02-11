from Bio import SeqIO
seq = SeqIO.parse(open("/mnt/hgfs/shared_folder/AF501235.fasta"), 'fasta')
print(type(seq))
for s in seq:
    print ("")
    print (type(s))
    print ("")
    print (s)
    print ("")