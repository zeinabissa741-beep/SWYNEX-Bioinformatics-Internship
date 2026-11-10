from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

from pathlib import Path

#reading and parsing fasta file
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
result = NCBIWWW.qblast("blastp", "nr", seq, 
                        hitlist_size=5)
blast = NCBIXML.read(result)


for alignment in blast.alignments:
    if "Homo sapiens" in alignment.hit_def:
        continue
    
    for hsp in alignment.hsps:
        print(f"Sequence: {alignment.title}")
        print(f"Score: {hsp.score}")
        print(f"length: {hsp.align_length}")
        print(f"Query: {hsp.query}")
        print(f"Subject: {hsp.sbjct}")
        print('\n')