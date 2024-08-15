#!/bin/bash
#SBATCH --mem=4G
#SBATCH -n 1
#SBATCH -N 1

eval $( spack load --sh bedtools2@2.30.0 )

GENOME=$1
WINDOWSIZE=$2
STEPS=$3
OUTPUT=$4

### Check if output already exists
if test -f "$OUTPUT"; then
echo "WARNING!!! output already exists"
fi
bedtools makewindows -g $GENOME -w $WINDOWSIZE -s $STEPS > $OUTPUT
echo "Complete!"
echo "Number of entries generated:"
wc -l $OUTPUT
