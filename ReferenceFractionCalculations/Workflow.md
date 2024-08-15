Start first with the genome size files of hg38 and the individual's genome

> ex: HG00621.maternal.ChromSize.txt

The create 500 base pair bins with no overlap across the individuals genome
> sbatch sliding_windows.sh HG00621.maternal.ChromSize.txt 500 500 Windows_HG00621_m.bed

Then, lift these bins over to HG38 using the PAF alignment of the 2 genomes and PAFtools
> sbatch run_LiftoverPAF.sh HG00621_mat.hg38.paf Windows_HG00621_m.bed Windows_HG00621_m_lifted_to_Hg38.bed

