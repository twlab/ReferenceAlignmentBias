import sys
import pysam


def extract_read_names_and_mapq(fastq_fileR1, fastq_fileR2 , bam_files, matF1, patF1):
    firstFile=True
    columns={}
    matReadsOne=[]
    matReadsTwo=[]
    patReadsOne=[]
    patReadsTwo=[]
    wentToMaternal=0
    wentToPaternal=0
    wentToBoth=0
 


    for bam_file in bam_files:
        read_mapq_dict = {}  # Create a dictionary to store mapQ scores for the current BAM file

        # Process the current BAM file and populate the dictionary with mapQ scores
        with pysam.AlignmentFile(bam_file, "rb") as bam:
            for read in bam:
                if read.is_secondary:
                    print(read)
                else:
                    if read.is_read1:
                        read_name = read.query_name+"/1"
                    else:
                        read_name = read.query_name+"/2"
                    if read.is_unmapped:
                        read_mapq_dict[read_name] = -1
                    else:
                        read_mapq_dict[read_name] = read.mapping_quality
                if firstFile:
                    if read.is_read1:
                        if read_mapq_dict[read_name] > 0 : #if mapped differentially to one location then place it where it belongs
                            if "maternal" in read.reference_name:
                                matReadsOne.append(read_name)
                                wentToMaternal+=1
                            else:
                                patReadsOne.append(read_name)
                                wentToPaternal+=1
                    else:
                        if read_mapq_dict[read_name] > 0: #if mapped differentially to one location then place it where it belongs
                            if "maternal" in read.reference_name:
                            
                                matReadsOne.append(read_name)
                                wentToMaternal+=1
                            else:
                        
                                patReadsOne.append(read_name)
                                wentToPaternal+=1
                

                    

        firstFile=False
        print("madeBamDict")
        print(bam_file) 
        print("Sizes- M1 M2 P1 P2")
        print(len(matReadsOne))
        print(len(matReadsTwo))
        print(len(patReadsOne))
        print(len(patReadsTwo))
        


       

        # Open the FASTQ file and create the tab-delimited output file
        print("open fastq 1")
        with open(fastq_fileR1, 'r') as fastq:
            for line_num, line in enumerate(fastq, 1):
                line = line.strip()
                if line_num % 4 == 1:  # Read name line
                    read_name = line[1:]  # Remove the "@" character
                    parts = read_name.split(" ")  # Split the string by space
                    read_name = parts[0]+"/1"
                    
                    mapq_score = read_mapq_dict.get(read_name, -1)
                    if read_name not in columns:
                        columns[read_name] = []
                    columns[read_name].append(str(mapq_score))

        with open(fastq_fileR2, 'r') as fastq:
            for line_num, line in enumerate(fastq, 1):
                line = line.strip()
                if line_num % 4 == 1:  # Read name line
                    read_name = line[1:]  # Remove the "@" character
                    parts = read_name.split(" ")  # Split the string by space
                    read_name = parts[0]+"/2"
                    
                    mapq_score = read_mapq_dict.get(read_name, -1)
                    if read_name not in columns:
                        columns[read_name] = []
                    columns[read_name].append(str(mapq_score))
        print(len(columns))
        



        

    for read_name in columns:
        mapq_scores = columns.get(read_name)
        if "/1" in read_name:
            if mapq_scores[0]=='0': #if muli in the combined
                if mapq_scores[1]!='-1' and mapq_scores[2]=='-1': #if 0 val -1
                    matReadsOne.append(read_name)
                    wentToMaternal+=1
                elif  mapq_scores[1]=='-1' and mapq_scores[2]!='-1': #if 0 -1 val
                    patReadsOne.append(read_name)
                    wentToPaternal+=1
                else:
                    matReadsOne.append(read_name)
                    patReadsOne.append(read_name)
                    wentToBoth+=1
            elif mapq_scores[0]=='-1': #if unmapped
                matReadsOne.append(read_name)
                patReadsOne.append(read_name)
                wentToBoth+=1 
        else:
            if mapq_scores[0]=='0': #if muli in the combined
                if mapq_scores[1]!='-1' and mapq_scores[2]=='-1': #if 0 val -1
                   
                    matReadsOne.append(read_name)
                    wentToMaternal+=1
                elif  mapq_scores[1]=='-1' and mapq_scores[2]!='-1': #if 0 -1 val
                   
                    patReadsOne.append(read_name)
                    wentToPaternal+=1
                else:
                    matReadsOne.append(read_name)
                    patReadsOne.append(read_name)
                    wentToBoth+=1  

            elif mapq_scores[0]=='-1': #if unmapped in combined
                matReadsOne.append(read_name)
                patReadsOne.append(read_name)
                wentToBoth+=1 

        
        
        
    print("Sizes- M1 M2 P1 P2")
    print(len(matReadsOne))
    print(len(matReadsTwo))
    print(len(patReadsOne))
    print(len(patReadsTwo))

    print("Mat, Pat, Both, TotalReads:")
    print(wentToMaternal)
    print(wentToPaternal)
    print(wentToBoth)
    print(len(columns))
    
    # print(wentToNeither)

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
bam_files = [sys.argv[3], sys.argv[4], sys.argv[5]] 
matFile1= sys.argv[6] 
patFile1= sys.argv[7] 

extract_read_names_and_mapq(fastq_fileR1, fastq_fileR2, bam_files, matFile1, patFile1)   
