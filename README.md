# SWYNEX-Bioinformatics-Internship
Analyzing biological datasets, visualizing findings, and completing a remote bioinformatics research report.<br>
## Documentation:<br>
### source: 
- Repository: NCBI Protein<br>
- Dataset accession number(s): NP_001435364<br>
- Dataset URL: [NCBI record link](https://www.ncbi.nlm.nih.gov/protein/NP_001435364.1?report=genpept)<br>
- Download date: November 2, 2026<br>
- Format: FASTA (.fasta)<br>
### size: 1kb<br>
### research question: "How conserved is the selected surfactant protein across different species, and which regions of its amino acid sequence show the highest degree of conservation?"<br>
### sequence similarity analysis:
#### methodology: 
* Performed a BLASTP search against the NCBI RefSeq Protein database.
* Restricted results to Mammalia, excluding Homo sapiens.
* Parsed the downloaded BLAST results using Biopython.
* Extracted accession numbers, species, percentage identity, query coverage, alignment length, E-values, and bit scores.
* Organized the top five sequence matches using pandas.<br>
#### research results:
* Total alignments retrieved: 7
* Top matches analyzed: 5
#### tools used:
* Python
* Biopython
* BLASTP
* Pandas
* NCBI RefSeq Protein<br>
### repository content:
* sequence.fasta - query protein sequence
* analysis.ipynb - protein analysis notebook
* SFTA3_top5_similar_proteins.csv - extracted BLASTP results<br>
### data interpreation:
The BLASTP results provide sequence similarity measurements between the query protein and matching non-human mammalian protein sequences.
Percentage identity, query coverage, and E-values can be used to assess the strength and extent of the sequence matches.
Further comparative analysis, such as multiple sequence alignment, is needed to identify conserved regions across species.
### data source:
[NCBI Protein Database](https://www.ncbi.nlm.nih.gov/protein/)
