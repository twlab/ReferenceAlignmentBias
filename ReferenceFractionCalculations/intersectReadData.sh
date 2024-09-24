#!/bin/bash
#SBATCH --mem=16G
binsBed=$1
BamFile=$2
chrSizeFile=$3
outputName=$4
path=$5
genomeName=$6

eval $( spack load --sh bedtools2@2.30.0 )
eval $( spack load --sh samtools@1.13) 
#ALL FILES MUST BE IN ORDER chr1 chr10 chr11 ... chr2 chr20...


# #For each entry in A, report the number of hits in B while restricting to -f. Reports 0 for A entries that have no overlap with B.

echo "$SECONDS"
samtools view -H "$BamFile"|grep @SQ|sed 's/@SQ\tSN:\|LN://g' > "$genomeName"genome.txt

 echo "$SECONDS"
 
    awk '{print $0"\t", FNR}' $binsBed > "$genomeName".temp.bed
    bedtools sort -i "$genomeName".temp.bed -faidx "$genomeName"genome.txt > "$binsBed".sorted.bed
    rm "$genomeName".temp.bed
 echo "$SECONDS" 


bedtools intersect -a "$binsBed".sorted.bed -b "$BamFile" -F 0.51 -c -sorted -g "$genomeName"genome.txt > "$outputName"

echo "$SECONDS"


# Now, resort resulting file back to original
 sort -k 4n  "$outputName" | awk -F "\t" '{print $1"\t"$2"\t"$3"\t"$5}' >  "$outputName".originalorder.bed
 
