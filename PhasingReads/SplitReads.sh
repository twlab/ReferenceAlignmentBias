#!/bin/bash
#SBATCH --mem=64G
#SBATCH -n 1
#SBATCH -N 1
eval $( spack load --sh seqtk@1.3)

read read1 read2 matOrPat output1 output2 prefix< <( sed -n ${SLURM_ARRAY_TASK_ID}p $1 )


sed -i 's|/.*||' $matOrPat 



split -l 1000000 "$matOrPat" "$prefix"

# Loop over the generated files
for f in "${prefix}"*; do
  # Sort and remove duplicates from each file
  sort -u "$f" > "${f}_sorted"
done

# Merge the sorted files into a final output file
sort -u "${prefix}"*_sorted > "${matOrPat}_sorted"
rm -f "${prefix}"*

seqtk subseq $read1 "${matOrPat}_sorted" > $output1
seqtk subseq $read2 "${matOrPat}_sorted" > $output2
