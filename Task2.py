from Bio import SeqIO
from Bio.Blast import NCBIXML
import pandas as pd

# reading and parsing fasta file
fasta_file = "sequence.fasta"
code = ""
seq = ""
for record in SeqIO.parse(fasta_file, "fasta"):
    code = record.id
    seq = str(record.seq).upper()

# how many a.a.
aa = len(seq)
print(f" {code} has {aa} amino acids\n")

# sequence similarity
print("----- performing sequence similarity -----\n")
with open("SFTA3_BLAST_results.xml") as result_handle:
    blast_record = NCBIXML.read(result_handle)
print("Number of alignments:", len(blast_record.alignments), "\n")
results = []

for alignment in blast_record.alignments:
    hsp = alignment.hsps[0]
    identity = (hsp.identities / hsp.align_length) * 100
    coverage = ((hsp.query_end - hsp.query_start + 1) / len(seq)) * 100
    description = alignment.hit_def
    species = description.split("[")[-1].replace("]", "")

    results.append(
        {
            "Accession": alignment.accession,
            "Species": species,
            "Description": description,
            "Identity (%)": round(identity, 2),
            "Coverage (%)": round(coverage, 2),
            "Alignment Length": hsp.align_length,
            "E-value": hsp.expect,
            "Bit Score": hsp.bits,
        }
    )
results = results[:5]

# tabling results
results_df = pd.DataFrame(results)
print(results_df)

results_df.to_csv("SFTA3_top5_similar_proteins.csv", index=False)
