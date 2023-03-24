#Split bam by chromosomes
for chrom in chr2 chr3 X Y
do
echo $chrom
    samtools view -bh $file ${chrom} >$file_${chrom}.bam
    samtools index $file_${chrom}.bam
done
