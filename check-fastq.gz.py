###This script will return True if the paired gzipped fastq files are complete, and False if they are not.
###Note: This script assumes that the fastq files are in the same order and that each read in the first file corresponds to the same read in the second file. 
import gzip
import argparse

# Create an argument parser object
parser = argparse.ArgumentParser()

# Add arguments to the parser
parser.add_argument('--input', required=True, help='Input file')
parser.add_argument('--output', required=False, help='Output file')

# Parse the command-line arguments
args = parser.parse_args()

# Print the values of the arguments
print(f"Checking the paired sample {args.input})
#print(args.output)


def is_fastq_complete(fastq1, fastq2):
    # Open the gzipped fastq files
    fq1 = gzip.open(fastq1, 'rb')
    fq2 = gzip.open(fastq2, 'rb')

    # Initialize counters for the number of lines in each file
    count1 = 0
    count2 = 0

    # Read through the first file, line by line
    for line in fq1:
        count1 += 1

    # Read through the second file, line by line
    for line in fq2:
        count2 += 1

    # Close the fastq files
    fq1.close()
    fq2.close()

    # Check if the number of lines in each file is a multiple of 4 (since each read has 4 lines in a fastq file)
    return count1 % 4 == 0 and count2 % 4 == 0

# Test the function with some sample gzipped fastq files
file1=str(args.input+'_1.fastq.gz')
file2=str(args.input+'_2.fastq.gz')
print(is_fastq_complete(file1,file2))

