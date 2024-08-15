#!/bin/bash
#SBATCH --mem=96G
#SBATCH --cpus-per-task=24
#SBATCH -n 1
#SBATCH -N 1


####SBATCH --array=1-10%10   # This will create 40 tasks numbered 1-40 and allow 10 concurrent jobs to run

# [Alignment parameters lookup file]
read THREADS REFERENCE READ1 READ2 OUTPUT < <( sed -n ${SLURM_ARRAY_TASK_ID}p $1 )
## COUNT TAKES ON VALUE OF TRUE OR FALSE

echo "Loading software..."
eval $( spack load --sh bwa@0.7.17 )
eval $( spack load --sh samtools@1.13 )

echo "Input files: "$READ1" "$READ2
echo "Reference: "$REFERENCE
echo "Number of threads: "$THREADS

echo "Starting Alignment..."

bwa mem -t $THREADS $REFERENCE $READ1 $READ2 | samtools view -bS - | samtools sort - -O 'bam' -o $OUTPUT


echo " Complete!"
