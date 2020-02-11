from Bio import AlignIO

alignment = AlignIO.read(open("/mnt/hgfs/shared_folder/7.example.aln"), "clustal")
for record in alignment:
    print ("%s - %s" % (record.seq, record.id))