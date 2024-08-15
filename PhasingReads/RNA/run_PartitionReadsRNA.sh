#!/bin/bash
#SBATCH --mem=64G
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=n.a.tekkey@wustl.edu

echo "Loading software..."

eval $( spack load --sh  python@3)
eval $( spack load --sh py-pysam@0.15.3/fhxd47q)

read FastQR1 FastQR2 CombinedBAM MatBAM PatBAM mat1 mat2 pat1 pat2 < <( sed -n ${SLURM_ARRAY_TASK_ID}p $1 )


#Unzip gzipped FastQs
echo "gunzipping..."
gunzip $FastQR1 $FastQR2
FastQR1_without_extension="${FastQR1%.gz}"
FastQR2_without_extension="${FastQR2%.gz}"
echo "unzipped..."



echo "Start python script..."
python3 /scratch/twlab/tekkey/PhasingData/scripts/partitionReadsRNA.py $FastQR1_without_extension $FastQR2_without_extension $CombinedBAM $MatBAM $PatBAM $mat1 $mat2 $pat1 $pat2
echo "Python script complete!"
