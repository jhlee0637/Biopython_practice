from Bio.Align.Applications import MuscleCommandline

muscle_exe = "~/muscle64"
cmd_line = MuscleCommandline(muscle_exe, input="/mnt/hgfs/shared_folder/HBA.all.fasta", out = "HBA.aln", clw=" ")

print(cmd_line)

stdout, stderr = cmd_line()