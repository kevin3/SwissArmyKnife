import csv,sys,glob
###USAGE:  python2.7
###Create fake fastq file from Illumina Infinium manifest file
agfile=glob.glob("test.csv")
reader3 = csv.DictReader(open(agfile[0]),delimiter=',',quotechar='"')
dumpline_counter=0
#for loop to insert into sqlite db
for line in reader3:
    Name=line['Name']
    #SourceSeq=line['AlleleA_ProbeSeq']
    #leftseqAR='@',Name,'_AlleleA_ProbeSeq'
    #print "".join(leftseqAR) #fasta seq name for left flanking seq
    #print SourceSeq
    #leftseqAR_len=int(len(SourceSeq))# length of left flanking seq
    #print "+"
    #print "~"*leftseqAR_len

    #SourceSeq=line['AlleleB_ProbeSeq']
    #leftseqAR='@',Name,'_AlleleB_ProbeSeq'
    #print "".join(leftseqAR) #fasta seq name for left flanking seq
    #print SourceSeq
    #leftseqAR_len=int(len(SourceSeq))# length of left flanking seq
    #print "+"
    #print "~"*leftseqAR_len

    SourceSeq=line['SourceSeq']
    leftseqAR='@',Name,'SourceSeq'
    print "".join(leftseqAR) #fasta seq name for left flanking seq
    print SourceSeq
    leftseqAR_len=int(len(SourceSeq))# length of left flanking seq
    print "+"
    print "~"*leftseqAR_len
