#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATION=BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "*** Processing $SAMPLE"
  cp ../rawdata/$SAMPLE.fastq .
  fastqc $SAMPLE.10k.fastq
  hisat2 -p $THREADS -x ../genomes/BDPG6 -U $SAMPLE.10k.fastq -S $SAMPLE_map.sam
  samtools sort -@ $THREADS $SAMPLE_map.sam -o $SAMPLE_map.bam
  samtools index $SAMPLE_map.bam
  stringtie  $SAMPLE_map.bam -e -B -p $THREADS -G ../genomes/BDGP6.Ensembl.81.gtf -o $SAMPLE_map.gtf
done
