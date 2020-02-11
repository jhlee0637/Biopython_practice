from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
sample_1 = SeqIO.read(open("/mnt/hgfs/shared_folder/AJ011404.gb"), "genbank")
sample_2 = SeqIO.read(open("/mnt/hgfs/shared_folder/AJ011405.gb"), "genbank")
sample_3 = SeqIO.read(open("/mnt/hgfs/shared_folder/AJ011408.gb"), "genbank")

list = [sample_1, sample_2, sample_3]
aln_fasta=""
for sample in list:
    title = sample.name+" "+sample.description
    aln_fasta+=">"+title+"\n"+sample.seq+"\n"
fr = open("aln_fasta", "w")
fr.write(str(aln_fasta))
fr.close()

from Bio.Align.Applications import MuscleCommandline
muscle_exe = "~/muscle64"
cmd_line = MuscleCommandline(muscle_exe, input="aln_fasta", out="7.8.aln", clw=" ")
print (cmd_line)
stdout, stderr = cmd_line()

from Bio import AlignIO
from Bio.motifs import Motif
from Bio import motifs
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
alignment = AlignIO.read("7.8.aln", "clustal")
instance=[]
for record in alignment:
    s = Seq(str(record.seq), IUPAC.unambiguous_dna)
    instance.append(s)
m =motifs.create(instance)
Motif.weblogo(m, '7.8_weblogo.png')