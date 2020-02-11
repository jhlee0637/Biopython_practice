from Bio import SeqIO
gbk = SeqIO.read(open("/mnt/hgfs/shared_folder/J01636.gbk"), "genbank")
print (type(gbk))
print (gbk)