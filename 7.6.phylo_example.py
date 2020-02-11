from Bio import Phylo
tree = Phylo.read("HBA.newick", "newick")
print(tree)
Phylo.draw(tree)
