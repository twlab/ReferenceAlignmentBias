# Reference Alignment Bias
## Workflow used to quantify Reference Alignment Bias for different functional genomic assays in *Quantifying Reference Alignment Bias in Functional Genomics Analyses* (Under Review at Cell Reports Methods)

*This code was specifically generated for the parameters of the study, and any end users may need to modify it to fit their specific use case.*

<p align="center">
<img width="500"  alt="Fig1WorkflowGitHub" src="https://github.com/user-attachments/assets/8e16805c-cf08-4e5b-ae55-414b2c6ff6c5" />
</p>

### *Phasing Reads*
To make the assumption that a read comes from one of the individual's haplotypes, the bulk reads must be phased based on the likelihood they originated from the maternal or paternal genome. Phasing was accomplished by leveraging MAPQ scores returned from alignments to the maternal, paternal, or maternal+paternal combined genomes.
