# Reference Alignment Bias
## Workflow used to quantify Reference Alignment Bias for different functional genomic assays in *Quantifying Reference Alignment Bias in Functional Genomics Analyses* [Manuscript under review at Cell Reports Methods]

*This code was specifically generated for the parameters of the study, and any end users may need to modify it to fit their specific use case.*

<p align="center">
<img width="500"  alt="Fig1WorkflowGitHub" src="https://github.com/user-attachments/assets/8e16805c-cf08-4e5b-ae55-414b2c6ff6c5" />
</p>

---

### *Phasing Reads*
To make the assumption that a read comes from one of the individual's haplotypes, the bulk reads must be phased based on the likelihood they originated from the maternal or paternal genome. Phasing was accomplished by leveraging MAPQ scores returned from alignments to the maternal, paternal, or maternal+paternal combined genomes. The exact commands used to split reads between maternal and paternal genomes can be accessed [here](PhasingReads/), and the detailed methods in Tekkey et al.

---
### *Calculating Reference Alignent Bias Fractions*
Reference alignment bias was measured through the following process:
1. Split the query genome into 500 bp bins (query being the individual haplotype from which the sequencing reads were generated).
2. Lift the bins over to the reference genome to get syntenic bin pairs.
3. Intersect reference and query bins with the reads aligned to that genome to get a count.
4. Calculate the reference fraction by dividing the number of reads intersecting the reference by the sum of reads intersecting the reference and query.

The exact commands used for this process can be accessed [here](ReferenceFractionCalculations/), and the detailed methods in Tekkey et al.
