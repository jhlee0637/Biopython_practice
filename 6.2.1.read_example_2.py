from Bio import SeqIO
seq = SeqIO.parse(open("/mnt/hgfs/shared_folder/SRR000982.fastq"), "fastq")
for s in seq:
    print (s.seq)