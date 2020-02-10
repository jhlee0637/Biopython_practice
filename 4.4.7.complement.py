seq ="TATAAAGGCAATATGCAGTAG"
comp_dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
comp_seq = ""
for s in seq:
    comp_seq += comp_dic[s]
revcomp_seq = comp_seq[::-1]
print(comp_seq)
print(revcomp_seq)