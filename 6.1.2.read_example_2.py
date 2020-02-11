from Bio import SeqIO
seq = SeqIO.read(open("/mnt/hgfs/shared_folder/MH464856.fasta"), "fasta")
print(type(seq))
print("----------")
print(seq)