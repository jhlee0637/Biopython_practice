from Bio import AlignIO
alignment = AlignIO.read(open("/mnt/hgfs/shared_folder/7.example.aln"), "clustal")
print (alignment)

