from Bio import SeqIO
seq = SeqIO.read(open("/mnt/hgfs/shared_folder/HM6240861.gb"), 'genbank')
print(seq)
print(len(seq))