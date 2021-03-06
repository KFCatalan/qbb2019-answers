mkdir oct11

conda create -n macs2 macs2
source activate macs2
wget chr19.fa.gz
wget http://hgdownload.soe.ucsc.edu/goldenPath/mm10/chromosomes/chr19.fa.gz
conda install bowtie2
bowtie2-build
wget http://67.207.142.119/outgoing/g1e.tar.xz
tar xvzf g1e.tar.xz 
gunzip chr19.fa.gz 


bowtie2-build -f chr19.fa referencechr

bowtie2 -x referencechr -U CTCF_G1E.fastq -S CTCF_G1E.sam
bowtie2 -x referencechr -U input_G1E.fastq -S input_ER4.sam
bowtie2 -x referencechr -U input_ER4.fastq -S input_G1E.sam
bowtie2 -x referencechr -U input_G1E.fastq -S input_G1E.sam

callpeak
conda install samtools
conda install bedtools
 
samtools view -Sb input_ER4.sam > input_.bam
samtools view -Sb input_G1E.sam > input_G1E.bam
samtools view -Sb CTCF_G1E.sam > CTCF_G1E.bam
samtools view -Sb CTCF_ER4.sam > CTCF_ER4.bam
samtools sort CTCF_ER4.bam > CTCF_ER4.bam
samtools sort input_ER4.bam > input_ER4.bam
samtools sort input_G1E.bam > input_G1E.bam
samtools sort CTCF_G1E.bam > CTCF_G1E.bam

macs2 callpeak -f BAM -t CTCF_G1E.bam -c input_G1E.bam -g 62309240 --outdir callpeaks_output_G1E
macs2 callpeak -f BAM -t CTCF_ER4.bam -c input_ER4.bam -g 62309240 --outdir callpeaks_output_ER4
 
cut -f 1,2,3,4,5,6 NA_peaks.narrowPeak > /Users/cmdb/oct11/mini_ER4
cut -f 1,2,3,4,5,6 NA_peaks.narrowPeak > /Users/cmdb/oct11/mini_G1E
 
bedtools intersect -v -a mini_ER4 -b mini_G1E > differential_binding_CTCF 
 
 
 
Feature overlap:
 
 
 > ./overlap.py overlap_ER4 overlap_G1E differential_binding_CTCF differential_binding_CTCF_work 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 