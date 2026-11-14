from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd

# reading and parsing fasta file
fasta_file = "sequence.fasta"
code = ""
seq = ""
for record in SeqIO.parse(fasta_file, "fasta"):
    code = record.id
    seq = str(record.seq).upper()

x = ProteinAnalysis(seq)
#Physicochemical analysis
result = []
result.append(
        {
            "Metric": "result",
            "Molecular Weight": "%0.2f" % x.molecular_weight(),
            "Aromaticity": "%0.2f" % x.aromaticity(),
            "Instability Index": "%0.2f" % x.instability_index(),
            "Gravy": "%0.2f" % x.gravy(),
            "Isoelectric Point": "%0.2f" % x.isoelectric_point(),
            "Charge at pH": "%0.2f" % x.charge_at_pH(7),
        }
)
results_df = pd.DataFrame(result)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(results_df)
print(x.count_amino_acids())