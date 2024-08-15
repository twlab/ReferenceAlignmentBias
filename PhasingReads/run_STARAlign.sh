#!/bin/bash
#SBATCH --mem=96G
#SBATCH --cpus-per-task=24
#SBATCH --mail-type=ALL
#SBATCH --mail-user=n.a.tekkey@wustl.edu

genomeDir=$1
genomeFasta=$2
GTFFile=$3
read1=$4
read2=$5

eval $( spack load --sh  star@2.7.11a)

echo "starting..."


STAR --runThreadN ${SLURM_CPUS_PER_TASK} --runMode genomeGenerate --genomeDir  $genomeDir --genomeFastaFiles $genomeFasta --sjdbGTFfile $GTFFile --sjdbOverhang 100
echo "done indexing now aligning.."
STAR --runThreadN ${SLURM_CPUS_PER_TASK} --genomeDir $genomeDir  --readFilesIn $read1 $read2 --readFilesCommand gunzip -c
echo "done"
 
