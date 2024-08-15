#!/bin/bash
#SBATCH --mem=32G
#SBATCH -n 1
#SBATCH -N 1

# Takes in the name of  the fasta file to be indexed and indexes it with bwa  (bwa index). It will do this in the directory that it is run in. So run it in the same directory you want the index to be in.
eval $( spack load --sh bwa@0.7.17 )

FASTA=$1

bwa index $FASTA

echo "Complete"


