from Bio import SeqIO
seq = SeqIO.parse(open("/mnt/hgfs/shared_folder/SRR000982.fastq"), "fastq")
print (type(seq))
for s in seq:
    print ("")
    print (type(s))
    print ("")
    print (s)
    print ("")