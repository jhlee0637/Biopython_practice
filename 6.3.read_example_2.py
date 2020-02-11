from Bio import SeqIO
gbk = SeqIO.read(open("/mnt/hgfs/shared_folder/J01636.gbk"), "genbank")
print (gbk.id)
print (gbk.description)
print (gbk.annotations['molecule_type'])
print (gbk.annotations['organism'])