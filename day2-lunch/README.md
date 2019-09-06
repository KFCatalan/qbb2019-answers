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

You retrieve the specified term from the file, cutting on field 3, you then sort it and use uniq -c to to filter out repeats


cut -f 3 SRR072893_map.sam | sort | uniq -c

You skip the grep step in order to pull up the file faster but it is now not in a list


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


You use python code to enumerate the file, skip the "@" and "*" rows and organize it by tabs delimited. The counter helps in keeping track of the number of alignments as well. This bis the fastest method because of its python basis.

#Exercise 4

The difference among categories is the number of flags with each category where reads that aligned had flags such as MD, NH, etc.. The alignments that had issues or did not function properly were labeled as YT or YF.










