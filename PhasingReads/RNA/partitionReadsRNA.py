import sys
import pysam


def extract_read_names_and_mapq(fastq_fileR1, fastq_fileR2 , bam_files, matF1, patF1):
 

    matReadsOne=[]
    patReadsOne=[]
    wentToMaternal=0
    wentToPaternal=0
    wentToBoth=0


    bam_file=bam_files[0]

    read_mapq_dict = {}  # Create a dictionary to store mapQ scores for the current BAM file
    read_mapq_dict_secondary = {}  # Create a dictionary to store mapQ scores for the current BAM file
    readUsed = {}  # Create a dictionary to store if we have put a read in a place or not

    with pysam.AlignmentFile(bam_file, "r") as bam:
        for read in bam:
            if read.is_secondary:
                if read.is_read1:
                    read_name = read.query_name+"/1"
                else:
                    read_name = read.query_name+"/2"
                if read.is_unmapped:
                    read_mapq_dict_secondary[read_name] = -1
                else:
                    read_mapq_dict_secondary[read_name] = read.mapping_quality
            else:
                if read.is_read1:
                    read_name = read.query_name+"/1"
                else:
                    read_name = read.query_name+"/2"
                if read.is_unmapped:
                    read_mapq_dict[read_name] = -1
                else:
                    read_mapq_dict[read_name] = read.mapping_quality

        
        # Open the FASTQ file and create the tab-delimited output file
        print("open fastq 1")
        with open(fastq_fileR1, 'r') as fastq:
            for line_num, line in enumerate(fastq, 1):
                line = line.strip()
                if line_num % 4 == 1:  # Read name line
                    read_name = line[1:]  # Remove the "@" character
                    parts = read_name.split(" ")  # Split the string by space
                    read_name = parts[0]+"/1"
                    readUsed[read_name]=-1  #put read in dict as unused
                    if read_name not in read_mapq_dict:
                        read_mapq_dict[read_name] = -1
                    read_name = parts[0]+"/2"
                    readUsed[read_name]=-1
                    if read_name not in read_mapq_dict:
                        read_mapq_dict[read_name] = -1
        
    with pysam.AlignmentFile(bam_file, "r") as bam:
        for read in bam:
            if not read.is_secondary:   #for every primary read
                if read.is_read1:
                    read_name = read.query_name+"/1"
                else:
                    read_name = read.query_name+"/2"
                readUsed[read_name]=1 #mark read as used
                if read_name not in read_mapq_dict_secondary:   #if no secondary alignment
                    if "maternal" in read.reference_name:
                       matReadsOne.append(read_name)
                       wentToMaternal+=1
                    else:
                       patReadsOne.append(read_name)
                       wentToPaternal+=1
                else:
                    if read_mapq_dict[read_name]>read_mapq_dict_secondary[read_name]: #if the map q of primary is better
                        if "maternal" in read.reference_name:
                            matReadsOne.append(read_name)
                            wentToMaternal+=1
                        else:
                            patReadsOne.append(read_name)
                            wentToPaternal+=1
                    else:   #otherwise give to both
                        matReadsOne.append(read_name)
                        patReadsOne.append(read_name)
                        wentToBoth+=1

    
    print("Adding the reads that did not map to both files")
    with open(fastq_fileR1, 'r') as fastq:
        for line_num, line in enumerate(fastq, 1):
            line = line.strip()
            if line_num % 4 == 1:  # Read name line
                read_name = line[1:]  # Remove the "@" character
                parts = read_name.split(" ")  # Split the string by space
                read_name = parts[0]+"/1"
                if readUsed[read_name]==-1:
                    matReadsOne.append(read_name)
                    patReadsOne.append(read_name)
                    wentToBoth+=1
                read_name = parts[0]+"/2"
                if readUsed[read_name]==-1:
                    matReadsOne.append(read_name)
                    patReadsOne.append(read_name)
                    wentToBoth+=1


    print(len(readUsed))

    print("Sizes- M1 M2 P1 P2")
    print(len(matReadsOne))
    print(len(patReadsOne))

    print("Mat, Pat, Both, None:")
    print(wentToMaternal)
    print(wentToPaternal)
    print(wentToBoth)
    
    


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
bam_files = [sys.argv[3], sys.argv[4], sys.argv[5]]  # Replace with your input BAM files
matFile1= sys.argv[6] 
patFile1= sys.argv[7] 

extract_read_names_and_mapq(fastq_fileR1, fastq_fileR2, bam_files, matFile1, patFile1)   
    

                    
