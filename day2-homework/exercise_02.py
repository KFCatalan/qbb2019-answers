#!/usr/bin/env python3

#Write a python script for identifier mapping. Your script should take as input the mapping file (as above) and a c_tab file from StringTie and find the corresponding translation from the mapping file. If found, it should print the line from the c_tab file with the identifier. If not found, it should do one of two things depending on a command line argument:
    # Print nothing (ignore the line)
    # Print and fill the field with a default value

import sys
import numpy
import scipy.stats

# Dictionary takes flybase column and matches it to its corresponding AC

c_tab_file="../results/stringtie/SRR072893/t_data.ctab"

f = open(c_tab_file, 'r')



translation = {}
with open("exercise_01_output", "r") as file:
    for line in file:
        FlyBase, UniprotID = line.strip().split("\t")
        translation[FlyBase] = UniprotID
# print(translation)

for line in f:
    columns = line.rstrip("\n").split()
    gene_id = columns[8] 
    if gene_id in translation:
       UniprotID = translation[gene_id]
       print(line.rstrip("\n") + "\t" + UniprotID)
    elif len(sys.argv) < 2:
        continue
    elif sys.argv[1] == "default":
        print(line.rstrip("\n") + "\t" + "Not Available")
    else:
        continue
        



#Enter ./exercise_02.py default to run


    
    
    
    
    
    
    