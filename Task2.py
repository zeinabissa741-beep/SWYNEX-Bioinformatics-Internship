from Bio import SeqIO
from pathlib import Path

fasta_file = "sequence.fasta"
code = ""
seq = ""

for record in SeqIO.parse(fasta_file, "fasta"):
    code = record.id
    seq = record.seq

#how many a.a.
aa = len(seq)
print(f" {code} has {aa} amino acids")

#sequence similarity