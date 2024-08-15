# contains no multimapped reads. Thus, to determine if a read belongs in mat or pat, 
#go through WGBS bam and give read to its paternal chromosome.
# Then, add all reads that were not in the bam to both.


#if multi in both, then it will go to both
#if multi in mat and unmapped in pat, it will go to both
#if unique in both and multi in combined, it will go to both
#basically, this is treating multimapped reads like unmapped reads and 
import sys
import pysam


def extract_read_names_and_mapq(fastq_fileR1, fastq_fileR2 , bam_fileCom, matF1, patF1):
   
 
    matReadsOne=[]
    patReadsOne=[]
    wentToMaternal=0
    wentToPaternal=0
    wentToBoth=0




    readUsed={}
  
    # in com file, put the parent in the inCom dictionary
    with pysam.AlignmentFile(bam_fileCom, "r") as bam:
        for read in bam:
            read_name_split=read.query_name.split("_")
            read_name_fix=read_name_split[0]
            if read.is_secondary:
                if read.is_read1:
                    read_name = read_name_fix+"/1"
                else:
                    read_name = read_name_fix+"/2"
            else:
                if read.is_read1:
                    read_name = read_name_fix+"/1"
                else:
                    read_name = read_name_fix+"/2"

                if "maternal" in read.reference_name:
                    matReadsOne.append(read_name)
                    readUsed[read_name_fix]=-1
                    wentToMaternal+=1
                else:
                    patReadsOne.append(read_name)
                    readUsed[read_name_fix]=-1
                    wentToPaternal+=1

        
        # Open the FASTQ file and create the tab-delimited output file
        print("open fastq 1")
        readNumbers=0
        with open(fastq_fileR1, 'r') as fastq:
            for line_num, line in enumerate(fastq, 1):
                line = line.strip()
                if line_num % 4 == 1:  # Read name line
                    readNumbers+=1
                    read_name = line[1:]  # Remove the "@" character
                    parts = read_name.split(" ")  # Split the string by space
                    read_name = parts[0]
                    # read_name = parts[0]+"/1"
                    if not read_name in readUsed:
                        read_name = parts[0]+"/1"
                        matReadsOne.append(read_name)
                        patReadsOne.append(read_name)
                        wentToBoth+=1
                   
        



    print("Sizes- M1 M2 P1 P2")
    print(len(matReadsOne))
    print(len(patReadsOne))

    print("Mat, Pat, Both, Total:")
    print(wentToMaternal)
    print(wentToPaternal)
    print(wentToBoth)
    print(readNumbers)
    
    
    with open(matF1, 'w') as file:
        # Write each list item to a new line
        for item in matReadsOne:
            file.write(str(item) + '\n')
    with open(patF1, 'w') as file:
        # Write each list item to a new line
        for item in patReadsOne:
            file.write(str(item) + '\n')


    
              


    


            
fastq_fileR1 = sys.argv[1]  
fastq_fileR2 = sys.argv[2]  
bam_file = sys.argv[3]  
matFile1= sys.argv[4] 
patFile1= sys.argv[5] 
extract_read_names_and_mapq(fastq_fileR1, fastq_fileR2, bam_file, matFile1, patFile1)
            
            
