Create a combined Genome file of maternal and paternal genome by renaming all chromosomes to be either maternal or paternal, and then cat the files together.

> sed 's/^>chr.*/&_maternal/' HG00741_mat_ragtag.fasta > HG00741_mat_ragtag_marked.fasta\
> sed 's/^>chr.*/&_paternal/' HG00741_pat_ragtag.fasta > HG00741_pat_ragtag_marked.fasta\
> cat HG00741_mat_ragtag_marked.fasta  HG00741_pat_ragtag_marked.fasta >  HG00741_combined.fasta


Then align reads to this combined genome using BWA-MEM:

> sbatch /scratch/twlab/tekkey/PhasingData/scripts/run_BWA_index.sh HG00741_combined.fasta
> Parameters.txt:
> > THREADS REFERENCE READ1 READ2 OUTPUT
> 
> sbatch --array=1-#%# /scratch/twlab/tekkey/PhasingData/scripts/run_Batch_BWAMEM.sh Parameters.txt

STAR:

> sbatch /scratch/twlab/tekkey/PhasingData/scripts/run_STARAlign.sh $genomeDir $genomeFasta $GTFFile $read1 $read2

Bismark:

> Run by John 

