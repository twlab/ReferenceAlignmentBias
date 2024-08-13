Create a parameter file with columns:
> FastQReads1 FastQReads2 CombinedBAM MatBAM PatBAM mat1Output mat2Output pat1Output pat2Output
Where CombinedBam is the aligne

> sbatch --array=1-#%# run_PartitionReads.sh ParamFile.
