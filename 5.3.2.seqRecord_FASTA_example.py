from Bio import SeqIO
record = SeqIO.read(open('/mnt/hgfs/shared_folder/J01636.fasta'), "fasta")
print (type(record))
print (record)