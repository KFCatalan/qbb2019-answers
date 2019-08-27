#Day 2 lunch

#Exercise 1

A) /Users/cmdb/qbb2019-answers/day2-lunch $ head -40000 SRR072893.fastq > SRR072893.10k.fastq


B) /Users/cmdb/qbb2019-answers/day2-lunch $ fastqc SRR072893.10k.fastq


C) /Users/cmdb/qbb2019-answers/day2-lunch $ hisat2 -p 4 -x ../genomes/BDPG6 -U SRR072893.10k.fastq -S SRR072893_map.sam


D) /Users/cmdb/qbb2019-answers/day2-lunch $ samtools sort -@ 4 SRR072893_map.sam -o SRR072893_map.bam

/Users/cmdb/qbb2019-answers/day2-lunch $ samtools index SRR072893_map.bam



E) /Users/cmdb/qbb2019-answers/day2-lunch $ stringtie SRR072893_map.bam -e -B -p 4 -G ../genomes/BDGP6.Ensembl.81.gtf -o SRR072893_map.gtf






#Exercise 3



grep "SRR072893" SRR072893_map.sam_ cut -f 3 | sort | uniq -c

cut -f 3 SRR072893_map.sam | sort | uniq -c



f = open('SRR072893_map.sam')
counter = 0
for i, line in enumerate( f ):
    if line.startswith("@"):
        continue
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    counter += 1
print (counter)



#Exercise 4













