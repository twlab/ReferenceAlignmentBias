# Reference Fraction Calculation
### This code details how the genome files were processed in order to calculate a reference fraction for syntenic bin pairs of the query genome and the reference.

### The general workflow is detailed below:

---


Start first with the genome size files of hg38 and the individual's genome

> ex: HG00621.maternal.ChromSize.txt

The create 500 base pair bins with no overlap across the individuals genome
> sbatch sliding_windows.sh HG00621.maternal.ChromSize.txt 500 500 Windows_HG00621_m.bed

Then, lift these bins over to HG38 using the PAF alignment of the 2 genomes and PAFtools
> sbatch run_LiftoverPAF.sh HG00621_mat.hg38.paf Windows_HG00621_m.bed Windows_HG00621_m_lifted_to_Hg38.bed

Then remove all flagged/random/alt/chrUn hits from the resulting liftover file and split the coordinates of the bin in hg38 and the individual into 2 seperate files, labled Trunc_Pattern_Windows
> grep -v 'random\|alt\|chrUn' Windows_HG00621_m_lifted_to_Hg38.bed > removedAlts.bed \
> awk -F "\t" '{print $1"\t"$2"\t"$3}'  removedAlts.bed  > HG38_Trunc_Pattern_Windows_HG00621_m_lifted_to_Hg38.bed \
> awk -F "\t" '{print $4}' removedAlts.bed > UNSEP_HG00621_m_Trunc_Pattern_Windows_HG00621_m_lifted_to_Hg38.bed \
> awk -F "_" '{print $1"\t"$2"\t"$3}' UNSEP_HG00621_m_Trunc_Pattern_Windows_HG00621_m_lifted_to_Hg38.bed > HG00621_m_Trunc_Pattern_Windows_HG00621_m_lifted_to_Hg38.bed \
> rm UNSEP_HG00621_m_Trunc_Pattern_Windows_HG00621_m_lifted_to_Hg38.bed \
> grep 'random\|alt\|chrUn' Windows_HG00621_m_lifted_to_Hg38.bed > Random_Alt_chrUn_Bins.bed \
> grep '_t3\|_t5' removedAlts.bed > T3T5_Bins.bed \
> awk -F "\t" '{print $4}' Windows_HG00621_m_lifted_to_Hg38.bed | awk -F "_" '{print $1"\t"$2"\t"$3}' > tabFormatTemp.bed \
> grep -v -f tabFormatTemp.bed  -w Windows_HG00621_m.bed > HG00621_m_CouldNotLift.bed \
> rm tabFormatTemp.bed

Then intersect the resulting bed files (individual and hg38) with read data. Do it for both A and B and maternal and paternal

> Parameters: binnedBedFile alignedReadsBamFile chromosomeSizeFile outputFile inPath genomeName

> sbatch intersectReadData.sh \\ \
>  HG00621_m_Trunc_Pattern_Windows_HG00621_m_lifted_to_Hg38.bed \\ \
>  HG00621_Mat_A.bam \\ \
>  HG00621.maternal.ChromSize.txt \\ \
>  HG00621_m_A_HG00621_m.bed \\ \
>  /scratch/twlab/tekkey/Liftovers/HG00621/mat/ATAC/A/ \\ \
>  HG00621_m


> sbatch intersectReadData.sh \\ \
> HG38_Trunc_Pattern_Windows_HG00621_m_lifted_to_Hg38.bed \\ \
>  hg38_HG00621_Mat_A.bam \\ \
>  hg38.25_chromsome.sizes \\ \
>   HG00621_m_A_hg38.bed \\ \
>   /scratch/twlab/tekkey/Liftovers/HG00621/mat/ATAC/A/ \\ \
>    hg38

Then combine the outputs of the intersection of hg38 and individual into a final outputfile
> Parameters: queryFile refFile queryName refName pathOut

> sbatch ScatteredToFrame.sh  \\ \
> HG00621_m_A_HG00621_m.bed.originalorder.bed  \\ \
> HG38_Trunc_Pattern_Windows_HG00621_m_lifted_to_Hg38.bed.originalorder.bed \\ \
> HG00621_m_A \\ \
> hg38  \\ \
> /scratch/twlab/tekkey/Liftovers/HG00621/mat/ATAC/A/


