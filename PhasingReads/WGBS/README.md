# General info

## Environment
Docker image used for WGBS analysis: `funchansu/wgbs:v2.0.5`

## Resource Requirements
- At least 100GB of RAM, 150GB recommended
- At least 16 threads

# Setup

## Pipeline configuration
`wgbs.smk` will require updates to several paths:
- `PHIX_REF`: path to the phiX174 phage genome .fasta
- `LAMBDA_DIR`: path to a directory containing a bismark-indexed & samtools-indexed lambda phage fasta
- `REF_DIR`: path to a directory containing a bismark-indexed & samtools-indexed reference fasta
- `repo_local_path`: path to a local installation of the repo/branch https://github.com/xzhuo/wgbs/tree/fan-branch, which contains some helper scripts

## Assembly indexing
- [Bismark indexing instructions](https://felixkrueger.github.io/Bismark/quick_reference/#genome-preparation)

## Specifying input reads
- The snakemake pipeline expects input fastq(s) to be within a directory called `fastq`, within the working directory specified by `WORKING_DIRECTORY` within `launch-wgbs.sh`
