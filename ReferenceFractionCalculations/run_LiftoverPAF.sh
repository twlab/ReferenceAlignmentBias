#!/bin/bash
#SBATCH --mem=32G

eval $( spack load --sh k8@0.2.4 ) 

alignment=$1
bed=$2
output=$3

echo "starting"

k8 /ref/hllab/software/paftools/paftools.js liftover -q 5 -l 100 -d 1 $alignment $bed > $output

echo "done"
